from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class ItemPedidoEntity(BaseEntity, UserMixin):
    __tablename__ = 'itens_pedidos'

    id_pedido = db.Column(db.Integer, db.ForeignKey(f'{schema}.pedidos.id'))
    id_produto = db.Column(db.Integer, db.ForeignKey(f'{schema}.produtos.id'))
    quantidade = db.Column(db.Integer, nullable=False)
    preco_unitario = db.Column(db.DECIMAL(10, 2), nullable=False)

    pedido = db.relationship('PedidoEntity', back_populates='item_pedido')
    produto = db.relationship('ProdutoEntity', uselist=False, back_populates='item_pedido')

    def __init__(self, 
        id_pedido: int,
        id_produto: int,
        quantidade: int,
        preco_unitario: float
        ) -> None:
        self.id_pedido = id_pedido
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def __repr__(self):
        return "<Item Pedido %r>" % self.id_produto
        
