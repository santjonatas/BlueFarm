import traceback
from app.application.config.global_repositories import GlobalRepositories
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.application.usecases.dto.input.entities.create_operador_input_dto import CreateOperadorInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.dto.input.users.update_perfil_user_input_dto import UpdatePerfilUserInputDto
from app.application.usecases.dto.out.users.create_operador_user_output_dto import CreateOperadorUserOutputDto
from app.application.usecases.dto.out.users.update_perfil_user_output_dto import UpdatePerfilUserOutputDto
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


repositories = GlobalRepositories()

class UpdatePerfilUserUseCase:
    def __init__(self,
        pessoa_service: PessoaService,
        usuario_service: UsuarioService,
        global_utils: GlobalUtils) -> None:
        self.pessoa_service = pessoa_service
        self.usuario_service = usuario_service
        self.global_utils = global_utils

    def execute(self, input_dto: UpdatePerfilUserInputDto, id_pessoa: int) -> bool:
        if input_dto.email != '':
            if not self.global_utils.regex_validator_util.verificar_email(email=input_dto.email):
                raise InvalidFieldException('Email inválido.')
        
        if input_dto.senha != None:
            if not self.global_utils.regex_validator_util.verificar_senha(senha=input_dto.senha):
                raise InvalidFieldException('Senha inválida.')
        
        if input_dto.email != '':
            if self.pessoa_service.pessoa_repository.email_exists(email=input_dto.email):
                raise UserAlreadyExistsException('Email em uso.')
        
        if input_dto.telefone != '':
            if self.pessoa_service.pessoa_repository.phone_number_exists(phone_number=input_dto.telefone):
                raise UserAlreadyExistsException('Telefone em uso.')

        if input_dto.senha!= None:
            input_dto.senha = self.global_utils.pwd_hasher_util.hash_password(password=input_dto.senha)

        try:
            try:
                pessoa_entity = repositories.pessoa_repository.atualizar_pessoa(
                    id=id_pessoa,
                    genero=input_dto.genero,
                    telefone=input_dto.telefone,
                    email=input_dto.email,
                    endereco=input_dto.endereco
                )
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise PessoaEntityException(str(e))

            try:
                usuario_entity = repositories.usuario_repository.atualizar_senha_usuario(
                    id_pessoa=id_pessoa,
                    nova_senha=input_dto.senha
                )
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise UsuarioEntityException(str(e))

        except PessoaEntityException:
            pass
        except UsuarioEntityException:
            self.pessoa_service.pessoa_repository.delete(id_pessoa)
        finally:
            return True
