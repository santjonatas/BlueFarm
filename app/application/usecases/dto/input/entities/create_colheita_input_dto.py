from datetime import datetime
from typing import Optional


class CreateColheitaInsumoInputDto:
    def __init__(self,
        id_cultivo: Optional[int] = None,
        id_produto: Optional[int] = None,
        quantidade: Optional[int] = None,
        data: Optional[str] = None
        ) -> None:
    
        self.id_cultivo = id_cultivo
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.data = data

    
    @property
    def to_dict(self) -> dict:
        return {
            'id_cultivo': self.id_cultivo if self.id_cultivo is not None else 0,
            'id_produto': self.id_produto if self.id_produto is not None else 0,
            'quantidade': self.quantidade if self.quantidade is not None else 0,
            'data': self.data if self.data is not None else ''
        }