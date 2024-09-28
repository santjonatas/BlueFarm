from datetime import datetime
from typing import Optional


class CreateProdutoInputDto:
    def __init__(self,
        nome: Optional[str] = None,
        descricao: Optional[str] = None,
        preco: Optional[str] = None
        ) -> None:
    
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

    
    @property
    def to_dict(self) -> dict:
        return {
            'nome': self.nome if self.nome is not None else '',
            'descricao': self.descricao if self.descricao is not None else '',
            'preco': self.preco if self.preco is not None else ''
        }