from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.usuario_entity import UsuarioEntity


class IUsuarioRepository(ABC, BaseRepository[UsuarioEntity]):
    pass
