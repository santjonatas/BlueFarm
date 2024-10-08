from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.departamento_entity import DepartamentoEntity


class IDepartamentoRepository(ABC, BaseRepository[DepartamentoEntity]):
    def get_by_departamento(self, area: str) -> DepartamentoEntity:
        ...
