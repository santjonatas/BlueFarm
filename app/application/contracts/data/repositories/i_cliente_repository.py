from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.cliente_entity import ClienteEntity


class IClienteRepository(ABC, BaseRepository[ClienteEntity]):
    pass