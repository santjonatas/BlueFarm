from app.application.settings.extensions import session

from app.models.data.repositories.usuario_management_repository.pessoa_repository import PessoaRepository
from app.models.data.repositories.usuario_management_repository.funcionario_repository import FuncionarioRepository
from app.models.data.repositories.usuario_management_repository.usuario_repository import UsuarioRepository
from app.models.data.repositories.usuario_management_repository.operador_repository import OperadorRepository

from app.models.entities.usuario_management.pessoa_entity import PessoaEntity
from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity
from app.models.entities.usuario_management.operador_entity import OperadorEntity


class RegistrarOperadorUseCase:
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

    def execute(self):

        pessoa_entity = PessoaEntity(
            nome=self.nome,
            data_nascimento= self.data_nascimento, 
            cpf= self.cpf, 
            genero= self.genero,
            telefone= self.telefone,
            email= self.email,
            endereco= self.endereco
        )
        pessoa_repository = PessoaRepository(session=session)
        pessoa = pessoa_repository.add(pessoa_entity)

        funcionario_entity = FuncionarioEntity(
            data_admissao= self.data_admissao,
            cargo= self.cargo,
            salario= self.salario,
            data_demissao= self.data_demissao,
            id_pessoa=pessoa.id
        )
        funcionario_repository = FuncionarioRepository(session=session)
        funcionario = funcionario_repository.add(funcionario_entity)

        usuario_entity = UsuarioEntity(
            username= self.username,
            senha= self.senha,
            permissao= self.permissao,
            id_funcionario=funcionario.id
        )
        usuario_repository = UsuarioRepository(session=session)
        usuario = usuario_repository.add(usuario_entity)

        operador_entity = OperadorEntity(
            area_operacao= self.area_operacao,
            supervisor_direto= self.supervisor_direto,
            id_usuario=usuario.id
        )
        operador_repository = OperadorRepository(session=session)
        operador_repository.add(operador_entity)

        pass