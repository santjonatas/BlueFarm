from app.domain.entities.pedido_entity import PedidoEntity


class CreatePedidoOutputDto:
    def __init__(self, pedido_entity: PedidoEntity) -> None:
        self.pedido_entity = pedido_entity
