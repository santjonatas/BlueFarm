import traceback
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_cliente_input_dto import CreateClienteInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.users.create_cliente_user_input_dto import CreateClienteUserInputDto
from app.application.usecases.dto.out.users.create_cliente_user_output_dto import CreateClienteUserOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.auth.UserAlreadyExistsException import UserAlreadyExistsException
from app.exceptions.database.ClienteEntityException import ClienteEntityException
from app.exceptions.database.PessoaEntityException import PessoaEntityException
from app.exceptions.database.UsuarioEntityException import UsuarioEntityException
from app.infra.services.database.cliente.cliente_service import ClienteService
from app.infra.services.database.pessoa.pessoa_service import PessoaService
from app.infra.services.database.usuario.usuario_service import UsuarioService
from app.infra.utils.security.crypto_util import CryptoUtil


class CreateClienteUserUseCase:
    def __init__(self,
        pessoa_service: PessoaService,
        usuario_service: UsuarioService,
        cliente_service: ClienteService,
        global_utils: GlobalUtils) -> None:
        self.pessoa_service = pessoa_service
        self.usuario_service = usuario_service
        self.cliente_service = cliente_service
        self.global_utils = global_utils

    def execute(self, input_dto: CreateClienteUserInputDto) -> CreateClienteUserOutputDto:
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
                    username=input_dto.username,
                    senha=input_dto.senha
                )

                usuario_entity = self.usuario_service.create(input_dto=usuario_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise UsuarioEntityException(str(e))

            try:
                cliente_input = CreateClienteInputDto(
                    id_usuario=usuario_entity.id,
                    status=True
                )

                cliente_entity = self.cliente_service.create(input_dto=cliente_input)

                print('Registrou tudo paizao')
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise ClienteEntityException(str(e))
        except PessoaEntityException:
            pass
        except UsuarioEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
        except ClienteEntityException:
            self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
            self.usuario_service.usuario_repository.delete(usuario_entity.id)
        finally:
            return CreateClienteUserOutputDto(cliente_entity=cliente_entity)
