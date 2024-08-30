from app.models.entities.usuario_management.usuario_entity import UsuarioEntity
from app.models.data.repositories.common.base_repository import BaseRepository


class IUsuarioRepository(BaseRepository[UsuarioEntity]):

    def obter_username(self, username: str) -> UsuarioEntity:
        ...

    def username_existe(self, username: str) -> bool:
        ...
    