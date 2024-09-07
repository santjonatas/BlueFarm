from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.cargo_entity import CargoEntity


class ICargoRepository(ABC, BaseRepository[CargoEntity]):
    def get_by_funcao(self, funcao: str) -> CargoEntity:
        ...
