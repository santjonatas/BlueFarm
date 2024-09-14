from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class InsumoEntity(BaseEntity, UserMixin):
    __tablename__ = 'insumos'

    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    preco = db.Column(db.DECIMAL(10, 2), nullable=False)
    comprado_em = db.Column(db.DateTime, nullable=False)


    cultivo = db.relationship('CultivoEntity', back_populates='insumo')

    def __init__(self,
        nome: str,
        descricao: str,
        preco: float,
        comprado_em: str,
        ) -> None:
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.comprado_em = comprado_em

    def __repr__(self):
        return "<Insumo %r>" % self.nome
