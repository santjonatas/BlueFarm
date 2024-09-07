from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.usuario_entity import UsuarioEntity


class IUsuarioRepository(ABC, BaseRepository[UsuarioEntity]):
    def get_by_username(self, username: str) -> UsuarioEntity:
        ...
    
    def username_exists(self, username: str) -> bool:
        ...
    