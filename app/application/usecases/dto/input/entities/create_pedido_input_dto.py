from datetime import datetime
from typing import Optional


class CreatePedidoInputDto:
    def __init__(self,
        id_cliente: Optional[int] = None,
        data_pedido: Optional[datetime] = None,
        status: Optional[str] = None,
        valor_total: Optional[str] = None
        ) -> None:
    
        self.id_cliente = id_cliente
        self.data_pedido = data_pedido
        self.status = status
        self.valor_total = valor_total

    
    @property
    def to_dict(self) -> dict:
        return {
            'id_cliente': self.id_cliente if self.id_cliente is not None else '',
            'data_pedido': self.data_pedido if self.data_pedido is not None else '',
            'status': self.status if self.status is not None else '',
            'valor_total': self.valor_total if self.valor_total is not None else ''
        }