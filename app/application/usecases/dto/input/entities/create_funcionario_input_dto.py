from datetime import datetime


class CreateFuncionarioInputDto:
    def __init__(self,
        data_admissao: datetime=None,
        id_cargo: int=None,
        id_pessoa: int=None) -> None:

        self.data_admissao = data_admissao
        self.id_cargo = id_cargo
        self.id_pessoa = id_pessoa
    
    @property
    def to_dict(self) -> dict:
        return {
            'data_admissao': self.data_admissao if self.data_admissao is not None else '',
            'id_cargo': self.id_cargo if self.id_cargo is not None else '',
            'id_pessoa': self.id_pessoa if self.id_pessoa is not None else ''
        }
