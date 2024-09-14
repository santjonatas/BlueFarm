from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.insumo_entity import InsumoEntity


class IInsumoRepository(ABC, BaseRepository[InsumoEntity]):
    pass