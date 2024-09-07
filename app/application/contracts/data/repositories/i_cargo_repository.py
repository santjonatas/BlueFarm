from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.cargo_entity import CargoEntity


class ICargoEntity(ABC, BaseRepository[CargoEntity]):
    pass
