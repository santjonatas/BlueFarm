from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class PedidoEntity(BaseEntity, UserMixin):
    __tablename__ = 'pedidos'

    id_cliente = db.Column(db.Integer, db.ForeignKey(f'{schema}.clientes.id'))
    data_pedido = db.Column(db.DateTime, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    valor_total = db.Column(db.Decimal, nullable=False)

    cliente = db.relationship('ClienteEntity', back_populates='pedido')
    item_pedido = db.relationship('ItensPedidosEntity', back_populates='pedido')
    pagamento = db.relationship('PagamentoEntity', uselist=False, back_populates='pedido')

    def __init__(self, 
        id_cliente: int,
        data_pedido: str,
        status: str,
        valor_total: float
        ) -> None:
        self.id_cliente = id_cliente
        self.data_pedido = data_pedido
        self.status = status
        self.valor_total = valor_total
        
    def __repr__(self):
        return "<Pedido %r>" % self.id