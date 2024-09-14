from requests import Session
from app.application.contracts.data.repositories.i_pedido_repository import IPedidoRepository
from app.domain.entities.pedido_entity import PedidoEntity


class PedidoRepository(IPedidoRepository):
    def __init__(self, session: Session):
        super().__init__(session, PedidoEntity)
