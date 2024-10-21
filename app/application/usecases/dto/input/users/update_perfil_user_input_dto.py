from datetime import datetime
from typing import Optional


class UpdatePerfilUserInputDto:
    def __init__(self,
        genero: Optional[str] = None,
        telefone: Optional[str] = None,
        email: Optional[str] = None,
        endereco: Optional[str] = None,
        senha: Optional[str] = None) -> None:
    
        # Atributos de CreatePessoaInputDto
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        
        # Atributos de CreateUsuarioInputDto
        self.senha = senha
        
