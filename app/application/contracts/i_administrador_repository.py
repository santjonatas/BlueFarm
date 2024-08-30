from app.models.data.repositories.common.base_repository import BaseRepository
from app.models.entities.usuario_management.administrador_entity import AdministradorEntity


class IAdministradorRepository(BaseRepository[AdministradorEntity]):
    pass
