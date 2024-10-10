from requests import Session
from app.application.contracts.data.repositories.i_pedido_repository import IPedidoRepository
from app.domain.entities.pedido_entity import PedidoEntity


class PedidoRepository(IPedidoRepository):
    def __init__(self, session: Session):
        super().__init__(session, PedidoEntity)

    def get_pedidos_by_cliente(self, id_cliente: int):
        return self.session.query(PedidoEntity)\
            .filter_by(id_cliente=id_cliente)\
            .order_by(PedidoEntity.id.desc())\
            .all()

    def atualizar_status(self, id_pedido: int, status: str) -> None:
        """
        Atualiza o status de um pedido no banco de dados com base no id_pedido.

        :param session: Sessão do banco de dados SQLAlchemy.
        :param id_pedido: ID do pedido a ser atualizado.
        :param status: Novo status a ser definido para o pedido.
        """
        pedido = self.session.query(PedidoEntity).filter(PedidoEntity.id == id_pedido).first()
        
        if pedido:
            pedido.status = status  
            self.session.commit() 

    def obter_pedidos_pagos(self):
        return self.session.query(PedidoEntity).filter_by(status='Pago').order_by(PedidoEntity.id.desc()).all()
    
    def obter_pedidos_nao_aguardando_pagamento(self):
        return self.session.query(PedidoEntity).filter(PedidoEntity.status != 'Aguardando Pagamento').order_by(PedidoEntity.id.desc()).all()