from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.produto_entity import ProdutoEntity


class IProdutoRepository(ABC, BaseRepository[ProdutoEntity]):
    pass