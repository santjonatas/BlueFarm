from datetime import datetime


class CreatePessoaInputDto:
    def __init__(self,
        nome: str=None, 
        data_nascimento: datetime=None, 
        cpf: str=None, 
        genero: str=None,
        telefone: str=None,
        email: str=None,
        endereco: str=None) -> None:
        
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    @property
    def to_dict(self) -> dict:
        return {
            'nome': self.nome if self.nome is not None else '',
            'data_nascimento': self.data_nascimento if self.data_nascimento is not None else '',
            'cpf': self.cpf if self.cpf is not None else '',
            'genero': self.genero if self.genero is not None else '',
            'telefone': self.telefone if self.telefone is not None else '',
            'email': self.email if self.email is not None else '',
            'endereco': self.endereco if self.endereco is not None else '',
        }