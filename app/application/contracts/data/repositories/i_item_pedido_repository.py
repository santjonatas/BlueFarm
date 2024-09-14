from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.item_pedido_entity import ItemPedidoEntity


class IItemPedidoRepository(ABC, BaseRepository[ItemPedidoEntity]):
    pass