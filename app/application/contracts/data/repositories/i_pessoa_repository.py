from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.pessoa_entity import PessoaEntity


class IPessoaRepository(ABC, BaseRepository[PessoaEntity]):
    pass
