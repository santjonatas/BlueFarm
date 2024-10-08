from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class DepartamentoEntity(BaseEntity):
    __tablename__ = 'departamentos'

    area = db.Column(db.String(50), nullable=False)

    administrador = db.relationship('AdministradorEntity', uselist=False, back_populates='departamento')

    def __init__(self, area: str) -> None:
        self.area = area

    def __repr__(self):
        return "<Departamento %r>" % self.area