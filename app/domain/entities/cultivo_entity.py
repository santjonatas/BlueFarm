from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class CultivoEntity(BaseEntity, UserMixin):
    __tablename__ = 'cultivo'

    id_insumo = db.Column(db.Integer, db.ForeignKey(f'{schema}.insumos.id'))
    quantidade = db.Column(db.Integer, nullable=False)
    data_inicio = db.Column(db.Date, nullable=True)
    data_fim = db.Column(db.Date, nullable=True)
    status = db.Column(db.String(50), nullable=False)


    colheita = db.relationship('ColheitaEntity', uselist=False, back_populates='cultivo')
    insumo = db.relationship('InsumoEntity', back_populates='cultivo')

    def __init__(self,
        id_insumo: int,
        quantidade: int,
        data_inicio: str,
        data_fim: str,
        status: str
        ) -> None:
        self.id_insumo = id_insumo
        self.quantidade = quantidade
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = status
        
    def __repr__(self):
        return "<Cultivo %r>" % self.id_insumo