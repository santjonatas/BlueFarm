from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class NivelEntity(BaseEntity):
    __tablename__ = 'niveis'

    id = db.Column(db.Integer, primary_key=True)
    acesso = db.Column(db.Boolean, nullable=False, default=False)


    cargos = db.relationship('CargosEntity', uselist=False, back_populates='niveis')

    def __init__(self,
            acesso: bool = False
            ) -> None:

        self.acesso = acesso