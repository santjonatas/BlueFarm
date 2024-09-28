import traceback
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.application.usecases.dto.input.entities.create_operador_input_dto import CreateOperadorInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.dto.out.users.create_operador_user_output_dto import CreateOperadorUserOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.auth.UserAlreadyExistsException import UserAlreadyExistsException
from app.exceptions.database.OperadorEntityException import OperadorEntityException
from app.exceptions.database.FuncionarioEntityException import FuncionarioEntityException
from app.exceptions.database.PessoaEntityException import PessoaEntityException
from app.exceptions.database.UsuarioEntityException import UsuarioEntityException
from app.infra.services.database.operador.operador_service import OperadorService
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.admin.admin_service import AdministradorService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.pessoa.pessoa_service import PessoaService
from app.infra.services.database.usuario.usuario_service import UsuarioService
from app.infra.utils.security.crypto_util import CryptoUtil


class CreateOperadorUserUseCase:
    def __init__(self,
        pessoa_service: PessoaService,
        funcionario_service: FuncionarioService,
        operador_service: OperadorService,
        usuario_service: UsuarioService,
        cargo_service: CargoService,
        administrador_service: AdministradorService,
        global_utils: GlobalUtils) -> None:
        self.pessoa_service = pessoa_service
        self.funcionario_service = funcionario_service
        self.operador_service = operador_service
        self.usuario_service = usuario_service
        self.cargo_service = cargo_service
        self.administrador_service = administrador_service
        self.global_utils = global_utils

    def execute(self, input_dto: CreateOperadorUserInputDto) -> CreateOperadorUserOutputDto:
        if not self.global_utils.regex_validator_util.verificar_email(email=input_dto.email):
            raise InvalidFieldException('Email inválido.')
        
        if not self.global_utils.regex_validator_util.verificar_senha(senha=input_dto.senha):
            raise InvalidFieldException('Senha inválida.')
        
        if not self.global_utils.document_util.validar_cpf(cpf=input_dto.cpf):
            raise InvalidFieldException('CPF inválido.')

        if self.pessoa_service.pessoa_repository.get_by_cpf(cpf=input_dto.cpf):
            raise UserAlreadyExistsException('CPF em uso.')
        
        if self.pessoa_service.pessoa_repository.email_exists(email=input_dto.email):
            raise UserAlreadyExistsException('Email em uso.')
        
        if self.pessoa_service.pessoa_repository.phone_number_exists(phone_number=input_dto.telefone):
            raise UserAlreadyExistsException('Telefone em uso.')
        
        if self.usuario_service.usuario_repository.username_exists(username=input_dto.username):
            raise UserAlreadyExistsException('Username em uso.')

        input_dto.senha = self.global_utils.pwd_hasher_util.hash_password(password=input_dto.senha)

        try:
            try:
                pessoa_input = CreatePessoaInputDto(
                    nome=input_dto.nome,
                    data_nascimento=input_dto.data_nascimento,
                    cpf=input_dto.cpf,
                    genero=input_dto.genero,
                    telefone=input_dto.telefone,
                    email=input_dto.email,
                    endereco=input_dto.endereco
                )

                pessoa_entity = self.pessoa_service.create(input_dto=pessoa_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise PessoaEntityException(str(e))

            try:
                usuario_input = CreateUsuarioInputDto(
                    id_pessoa=pessoa_entity.id,
                    username=f'{input_dto.username}@op',
                    senha=input_dto.senha
                )

                usuario_entity = self.usuario_service.create(input_dto=usuario_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise UsuarioEntityException(str(e))

            try:
                funcionario_input = CreateFuncionarioInputDto(
                    id_usuario=usuario_entity.id,
                    id_cargo=input_dto.cargo,
                    data_admissao=input_dto.data_admissao,
                )

                funcionario_entity = self.funcionario_service.create(input_dto=funcionario_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise FuncionarioEntityException(str(e))

            try:
                operador_input = CreateOperadorInputDto(
                    id_funcionario=funcionario_entity.id,
                    id_supervisor=input_dto.supervisor
                )

                operador_entity = self.operador_service.create(input_dto=operador_input)

                print('Registrou tudo paizao')
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise OperadorEntityException(str(e))
        except PessoaEntityException:
            pass
        except FuncionarioEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
        except UsuarioEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
            self.funcionario_service.funcionario_repository.delete(funcionario_entity.id)
        except OperadorEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
            self.funcionario_service.funcionario_repository.delete(funcionario_entity.id)
            self.usuario_service.usuario_repository.delete(usuario_entity.id)
        finally:
            return CreateOperadorUserOutputDto(operador_entity=operador_entity)
