from datetime import datetime
from typing import Optional


class CreateClienteUserInputDto:
    def __init__(self,
        nome: Optional[str] = None,
        data_nascimento: Optional[datetime] = None,
        cpf: Optional[str] = None,
        genero: Optional[str] = None,
        telefone: Optional[str] = None,
        email: Optional[str] = None,
        endereco: Optional[str] = None,
        username: Optional[str] = None,
        senha: Optional[str] = None,
        status: Optional[bool] = None) -> None:
    
        # Atributos de CreatePessoaInputDto
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
        # Atributos de CreateUsuarioInputDto
        self.username = username
        self.senha = senha
        
        # Atributos de CreateClienteInputDto
        self.status = status
