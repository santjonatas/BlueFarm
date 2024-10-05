from datetime import datetime
from typing import Optional


class CreateInsumoInputDto:
    def __init__(self,
        nome: Optional[str] = None,
        descricao: Optional[str] = None,
        preco: Optional[str] = None,
        comprado_em: Optional[datetime] = None,
        quantidade: Optional[int] = None,
        ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.comprado_em = comprado_em
        self.quantidade = quantidade
        
    @property
    def to_dict(self) -> dict:
        return {
            'nome': self.nome if self.nome is not None else '',
            'descricao': self.descricao if self.descricao is not None else '',
            'preco': self.preco if self.preco is not None else '',
            'comprado_em': self.comprado_em if self.comprado_em is not None else '',
            'quantidade': self.quantidade if self.quantidade is not None else 0
        }