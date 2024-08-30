from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity
from app.models.data.repositories.common.base_repository import BaseRepository


class IFuncionarioRepository(BaseRepository[FuncionarioEntity]):
    ...
