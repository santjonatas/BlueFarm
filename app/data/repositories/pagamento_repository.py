from requests import Session
from app.application.contracts.data.repositories.i_pagamento_repository import IPagamentoRepository
from app.domain.entities.pagamento_entity import PagamentoEntity


class PagamentoRepository(IPagamentoRepository):
    def __init__(self, session: Session):
        super().__init__(session, PagamentoEntity)
