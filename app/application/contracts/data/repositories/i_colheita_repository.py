from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.colheita_entity import ColheitaEntity


class IColheitaRepository(ABC, BaseRepository[ColheitaEntity]):
    pass