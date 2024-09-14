from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.cultivo_entity import CultivoEntity


class ICultivoRepository(ABC, BaseRepository[CultivoEntity]):
    pass