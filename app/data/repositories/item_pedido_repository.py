from requests import Session
from app.application.contracts.data.repositories.i_item_pedido_repository import IItemPedidoRepository
from app.domain.entities.item_pedido_entity import ItemPedidoEntity


class ItemPedidoRepository(IItemPedidoRepository):
    def __init__(self, session: Session):
        super().__init__(session, ItemPedidoEntity)

    def get_itens_by_pedido(self, id_pedido: int):
        return self.session.query(ItemPedidoEntity).filter_by(id_pedido=id_pedido).all()