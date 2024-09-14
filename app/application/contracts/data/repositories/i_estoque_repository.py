from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.estoque_entity import EstoqueEntity


class IEstoqueRepository(ABC, BaseRepository[EstoqueEntity]):
    pass