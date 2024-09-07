from datetime import datetime
from typing import Optional


class CreateAdminUserInputDto:
    def __init__(self,
        nome: Optional[str] = None,
        data_nascimento: Optional[datetime] = None,
        cpf: Optional[str] = None,
        genero: Optional[str] = None,
        telefone: Optional[str] = None,
        email: Optional[str] = None,
        endereco: Optional[str] = None,
        data_admissao: Optional[datetime] = None,
        cargo: Optional[str] = None,
        username: Optional[str] = None,
        senha: Optional[str] = None,
        departamento: Optional[str] = None) -> None:
    
        # Atributos de CreatePessoaInputDto
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

        # Atributos de CreateFuncionarioInputDto
        self.data_admissao = data_admissao
        self.cargo = cargo
        
        # Atributos de CreateUsuarioInputDto
        self.username = username
        self.senha = senha
        
        # Atributos de CreateAdministradorInputDto
        self.departamento = departamento
