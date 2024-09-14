from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class ProdutoEntity(BaseEntity, UserMixin):
    __tablename__ = 'produtos'

    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.DECIMAL(10, 2), nullable=False)


    item_pedido = db.relationship('ItemPedidoEntity', back_populates='produto')
    estoque = db.relationship('EstoqueEntity', uselist=False, back_populates='produto')
    colheita = db.relationship('ColheitaEntity', back_populates='produto')

    def __init__(self,
        nome: str,
        descricao: str,
        preco: float
        ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        
    def __repr__(self):
        return "<Produto %r>" % self.nome