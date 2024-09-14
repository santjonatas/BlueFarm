from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.pagamento_entity import PagamentoEntity


class IPagamentoRepository(ABC, BaseRepository[PagamentoEntity]):
    pass