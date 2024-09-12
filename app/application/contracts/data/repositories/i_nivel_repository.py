from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.nivel_enity import NivelEntity


class INivelRepository(ABC, BaseRepository[NivelEntity]):
    def get_by_acesso(self, acesso: bool) -> NivelEntity:
        ...
