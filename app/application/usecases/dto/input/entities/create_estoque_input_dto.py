from datetime import datetime
from typing import Optional


class CreateEstoqueInputDto:
    def __init__(self,
        id_produto: Optional[int] = None,
        quantidade_disponivel: Optional[int] = None,
        ultima_atualizacao: Optional[datetime] = None
        ) -> None:
    
        self.id_produto = id_produto
        self.quantidade_disponivel = quantidade_disponivel
        self.ultima_atualizacao = ultima_atualizacao

    
    @property
    def to_dict(self) -> dict:
        return {
            'id_produto': self.id_produto if self.id_produto is not None else '',
            'quantidade_disponivel': self.quantidade_disponivel if self.quantidade_disponivel is not None else '',
            'ultima_atualizacao': self.ultima_atualizacao if self.ultima_atualizacao is not None else ''
        }