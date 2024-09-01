from app.application.settings.extensions import session

from app.models.data.repositories.usuario_management_repository.pessoa_repository import PessoaRepository
from app.models.data.repositories.usuario_management_repository.funcionario_repository import FuncionarioRepository
from app.models.data.repositories.usuario_management_repository.usuario_repository import UsuarioRepository
from app.models.data.repositories.usuario_management_repository.operador_repository import OperadorRepository
from app.models.data.repositories.usuario_management_repository.administrador_repository import AdministradorRepository
from app.models.entities.usuario_management.pessoa_entity import PessoaEntity
from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity
from app.models.entities.usuario_management.operador_entity import OperadorEntity
from app.models.entities.usuario_management.administrador_entity import AdministradorEntity

from app.infra.utils.auth.regex_validator import RegexValidatorUtil
from app.infra.utils.auth.pwd_hasher import PwdHasherUtil

from app.exceptions.usuario_exceptions.formato_senha_invalido_exception import FormatoSenhaInvalidoException
from app.exceptions.usuario_exceptions.usuario_inexistente_exception import UsuarioInexistenteException
from app.exceptions.auth_exceptions.auth_exception import AuthException


regex = RegexValidatorUtil()
pwd_hasher = PwdHasherUtil()

class LoginInputDto:
    def __init__(self,  
                 username, 
                 senha
                ) -> None:
        self.username = username
        self.senha = senha
        pass


class LoginOutputDto:
    def __init__(self, 
                 pessoa: PessoaEntity, 
                 funcionario: FuncionarioEntity, 
                 usuario: UsuarioEntity,
                 operador: OperadorEntity = None,
                 administrador: AdministradorEntity = None
                 ) -> None:
        self.pessoa = pessoa
        self.funcionario = funcionario
        self.usuario = usuario
        self.operador = operador
        self.administrador = administrador
        pass


class LoginUseCase:
    def execute(self, input: LoginInputDto) -> LoginOutputDto:

        pessoa_repository = PessoaRepository(session=session)
        funcionario_repository = FuncionarioRepository(session=session)
        usuario_repository = UsuarioRepository(session=session)
        operador_repository = OperadorRepository(session=session)
        
        if not regex.verificar_senha(senha=input.senha):
            raise FormatoSenhaInvalidoException('Formato de senha inválida')

        if not usuario_repository.username_existe(username=input.username):
            raise UsuarioInexistenteException('Nenhum usuário encontrado com esse username')
    
        usuario_entrada = usuario_repository.obter_username(username=input.username)

        if not pwd_hasher.verify_password(hashed_password=usuario_entrada.senha, password=input.senha):
            raise AuthException('Senha inválida')
        
        # return LoginOutputDto(
        #     pessoa=pessoa_entity, 
        #     funcionario=funcionario_entity,
        #     usuario=usuario_entity,
        #     operador=operador_entity
        #     )
        pass