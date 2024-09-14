from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class NivelEntity(BaseEntity):
    __tablename__ = 'niveis'

    acesso = db.Column(db.Boolean, nullable=False, default=False)


    cargo = db.relationship('CargoEntity', back_populates='nivel')

    def __init__(self,
            acesso: bool = False
            ) -> None:

        self.acesso = acesso

    def __repr__(self):
        return "<Nível %r>" % self.acesso