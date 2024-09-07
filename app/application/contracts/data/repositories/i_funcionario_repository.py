from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.funcionario_entity import FuncionarioEntity


class IFuncionarioRepository(ABC, BaseRepository[FuncionarioEntity]):
    pass
