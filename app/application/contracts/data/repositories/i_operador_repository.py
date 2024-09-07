from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.operador_entity import OperadorEntity


class IOperadorRepository(ABC, BaseRepository[OperadorEntity]):
    pass
