from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.pedido_entity import PedidoEntity


class IPedidoRepository(ABC, BaseRepository[PedidoEntity]):
    pass