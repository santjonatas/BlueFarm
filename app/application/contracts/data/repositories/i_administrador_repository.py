from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.administrador_entity import AdministradorEntity


class IAdministradorRepository(ABC, BaseRepository[AdministradorEntity]):
    pass
