from app.application.settings.extensions import session

from app.models.data.repositories.usuario_management_repository.pessoa_repository import PessoaRepository
from app.models.data.repositories.usuario_management_repository.funcionario_repository import FuncionarioRepository
from app.models.data.repositories.usuario_management_repository.usuario_repository import UsuarioRepository
from app.models.data.repositories.usuario_management_repository.operador_repository import OperadorRepository
from app.models.entities.usuario_management.pessoa_entity import PessoaEntity
from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity
from app.models.entities.usuario_management.operador_entity import OperadorEntity

from app.infra.utils.auth.regex_validator import RegexValidatorUtil

from app.exceptions.usuario_exceptions.formato_email_invalido_exception import FormatoEmailInvalidoException
from app.exceptions.usuario_exceptions.formato_senha_invalido_exception import FormatoSenhaInvalidoException
from app.exceptions.usuario_exceptions.usuario_existente_exception import UsuarioExistenteException
from app.exceptions.usuario_exceptions.cpf_invalido_exception import CpfInvalidoException


regex = RegexValidatorUtil()

class RegistrarOperadorInputDto:
    def __init__(self, 
                  nome, 
                 data_nascimento, 
                 cpf, 
                 genero, 
                 telefone, 
                 email, 
                 endereco, 
                 data_admissao, 
                 cargo, 
                 salario,
                 data_demissao, 
                 username, 
                 senha,
                 permissao, 
                 area_operacao, 
                 supervisor_direto
                ) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.salario = salario
        self.data_demissao = data_demissao
        self.username = username
        self.senha = senha
        self.permissao = permissao
        self.area_operacao = area_operacao
        self.supervisor_direto = supervisor_direto
        pass


class RegistrarOperadorOutputDto:
    def __init__(self, 
                 pessoa: PessoaEntity, 
                 funcionario: FuncionarioEntity, 
                 usuario: UsuarioEntity,
                 operador: OperadorEntity
                 ) -> None:
        self.pessoa = pessoa
        self.funcionario = funcionario
        self.usuario = usuario
        self.operador = operador
        pass


class RegistrarOperadorUseCase:
    def execute(self, input: RegistrarOperadorInputDto) -> RegistrarOperadorOutputDto:

        pessoa_repository = PessoaRepository(session=session)
        funcionario_repository = FuncionarioRepository(session=session)
        usuario_repository = UsuarioRepository(session=session)
        operador_repository = OperadorRepository(session=session)

        if not regex.verificar_email(email=input.email):
            raise FormatoEmailInvalidoException('Formato de email inválido')
        
        if not regex.verificar_senha(senha=input.senha):
            raise FormatoSenhaInvalidoException('Formato de senha inválida')
        
        if pessoa_repository.email_existe(email=input.email):
            raise UsuarioExistenteException('Email em uso')
        
        if usuario_repository.username_existe(username=input.username):
            raise UsuarioExistenteException('Nome de usuário em uso')
        
        if pessoa_repository.telefone_existe(telefone=input.telefone):
            raise UsuarioExistenteException('Número de telefone em uso')
        
        if regex.validar_cpf(cpf=input.cpf) == False:
            raise CpfInvalidoException('CPF Inválido')
            
        if pessoa_repository.cpf_existe(cpf=input.cpf):
            raise UsuarioExistenteException('CPF em uso')
        

        pessoa_entity = PessoaEntity(
            nome=input.nome,
            data_nascimento= input.data_nascimento, 
            cpf= input.cpf, 
            genero= input.genero,
            telefone= input.telefone,
            email= input.email,
            endereco= input.endereco
        )
        pessoa = pessoa_repository.add(pessoa_entity)

        funcionario_entity = FuncionarioEntity(
            data_admissao= input.data_admissao,
            cargo= input.cargo,
            salario= input.salario,
            data_demissao= input.data_demissao,
            id_pessoa=pessoa.id
        )
        funcionario = funcionario_repository.add(funcionario_entity)

        usuario_entity = UsuarioEntity(
            username= input.username,
            senha= input.senha,
            permissao= input.permissao,
            id_funcionario=funcionario.id
        )
        usuario = usuario_repository.add(usuario_entity)

        operador_entity = OperadorEntity(
            area_operacao= input.area_operacao,
            supervisor_direto= input.supervisor_direto,
            id_usuario=usuario.id
        )
        operador_repository.add(operador_entity)
        
        return RegistrarOperadorOutputDto(
            pessoa=pessoa_entity, 
            funcionario=funcionario_entity,
            usuario=usuario_entity,
            operador=operador_entity
            )