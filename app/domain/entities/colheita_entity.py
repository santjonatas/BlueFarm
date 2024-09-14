from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class ColheitaEntity(BaseEntity, UserMixin):
    __tablename__ = 'colheita'

    id_cultivo = db.Column(db.Integer, db.ForeignKey(f'{schema}.cultivo.id'))
    id_produto = db.Column(db.Integer, db.ForeignKey(f'{schema}.produtos.id'))
    quantidade = db.Column(db.Integer, nullable=False)
    data = db.Column(db.DateTime, nullable=False)


    produto = db.relationship('ProdutoEntity', back_populates='colheita')
    cultivo = db.relationship('CultivoEntity', uselist=False, back_populates='colheita')

    def __init__(self,
        id_cultivo: int,
        id_produto: int,
        quantidade: int,
        data: str
        ) -> None:
        self.id_cultivo = id_cultivo
        self.id_produto = id_produto
        self.quantidade = quantidade
        self.data = data
        
    def __repr__(self):
        return "<Colheita %r>" % self.id_cultivo