from datetime import datetime
from typing import Optional


class CreateItemPedidoInputDto:
    def __init__(self,
        id_pedido: Optional[int] = None,
        id_produto: Optional[int] = None,
        quantidade: Optional[int] = None,
        preco_unitario: Optional[str] = None
        ) -> None:
    
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    
    @property
    def to_dict(self) -> dict:
        return {
            'id_pedido': self.id_pedido if self.id_pedido is not None else '',
            'id_produto': self.id_produto if self.id_produto is not None else '',
            'quantidade': self.quantidade if self.quantidade is not None else '',
            'preco_unitario': self.preco_unitario if self.preco_unitario is not None else ''
        }