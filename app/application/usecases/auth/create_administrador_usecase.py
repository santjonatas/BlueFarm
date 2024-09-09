from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_administrador_input_dto import CreateAdministradorInputDto
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.output.users.create_admin_user_output_dto import CreateAdminUserOutputDto
from app.exceptions.InvalidFieldException import InvalidFieldException
from app.exceptions.UserAlreadyExistsException import UserAlreadyExistsException
from app.exceptions.database.AdministradorEntityException import AdministradorEntityException
from app.exceptions.database.FuncionarioEntityException import FuncionarioEntityException
from app.exceptions.database.PessoaEntityException import PessoaEntityException
from app.exceptions.database.UsuarioEntityException import UsuarioEntityException
from app.infra.services.database.admin.admin_service import AdministradorService
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.pessoa.pessoa_service import PessoaService
from app.infra.services.database.usuario.usuario_service import UsuarioService


class CreateAdminUserUseCase:
    def __init__(self,
        pessoa_service: PessoaService,
        funcionario_service: FuncionarioService,
        administrador_service: AdministradorService,
        usuario_service: UsuarioService,
        cargo_service: CargoService,
        departamento_service: DepartamentoService,
        global_utils: GlobalUtils) -> None:
        self.pessoa_service = pessoa_service
        self.funcionario_service = funcionario_service
        self.administrador_service = administrador_service
        self.usuario_service = usuario_service
        self.cargo_service = cargo_service
        self.departamento_service = departamento_service
        self.global_utils = global_utils

    def execute(self, input_dto: CreateAdminUserInputDto) -> CreateAdminUserOutputDto:
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
        input_dto.cpf = self.global_utils.crypto_util.encrypt(value=input_dto.cpf)

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
                raise PessoaEntityException(str(e))

            try:
                funcionario_input = CreateFuncionarioInputDto(
                    data_admissao=input_dto.data_admissao,
                    id_cargo=input_dto.cargo,
                    id_pessoa=pessoa_entity.id
                )

                funcionario_entity = self.funcionario_service.create(input_dto=funcionario_input)
            except Exception as e:
                raise FuncionarioEntityException(str(e))

            try:
                usuario_input = CreateUsuarioInputDto(
                    id_funcionario=funcionario_entity.id,
                    username=input_dto.username,
                    senha=input_dto.senha
                )

                usuario_entity = self.usuario_service.create(input_dto=usuario_input)
            except Exception as e:
                raise UsuarioEntityException(str(e))

            try:
                administrador_input = CreateAdministradorInputDto(
                    id_usuario=usuario_entity.id,
                    id_departamento=input_dto.departamento
                )

                administrador_entity = self.administrador_service.create(input_dto=administrador_input)
            except Exception as e:
                raise AdministradorEntityException(str(e))
        except PessoaEntityException:
            pass
        except FuncionarioEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
        except UsuarioEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
            self.funcionario_service.funcionario_repository.delete(funcionario_entity.id)
        except AdministradorEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
            self.funcionario_service.funcionario_repository.delete(funcionario_entity.id)
            self.usuario_service.usuario_repository.delete(usuario_entity.id)
        finally:
            print('Registrou tudo paizao')

        return CreateAdminUserOutputDto(admin_entity=administrador_entity)
