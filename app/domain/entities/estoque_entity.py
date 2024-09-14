from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class EstoqueEntity(BaseEntity, UserMixin):
    __tablename__ = 'estoque'

    id_produto = db.Column(db.Integer, db.ForeignKey(f'{schema}.produtos.id'))
    quantidade_disponivel = db.Column(db.Integer, nullable=False)
    ultima_atualizacao = db.Column(db.DateTime, nullable=False)


    produto = db.relationship('ProdutoEntity', uselist=False, back_populates='estoque')

    def __init__(self,
        id_produto: int,
        quantidade_disponivel: int,
        ultima_atualizacao: str
        ) -> None:
        self.id_produto = id_produto
        self.quantidade_disponivel = quantidade_disponivel
        self.ultima_atualizacao = ultima_atualizacao
        
    def __repr__(self):
        return "<Estoque %r>" % self.id_produto