from requests import Session
from app.application.contracts.data.repositories.i_pagamento_repository import IPagamentoRepository
from app.domain.entities.pagamento_entity import PagamentoEntity


class PagamentoRepository(IPagamentoRepository):
    def __init__(self, session: Session):
        super().__init__(session, PagamentoEntity)

    def get_pagamento_by_id_pedido(self, id_pedido: int):
        """
        Busca um pagamento no banco de dados com base no id_pedido.

        :param session: Sessão do banco de dados SQLAlchemy.
        :param id_pedido: ID do pedido a ser buscado.
        :return: Instância de PagamentoEntity ou None se não encontrado.
        """
        return self.session.query(PagamentoEntity).filter(PagamentoEntity.id_pedido == id_pedido).first()
