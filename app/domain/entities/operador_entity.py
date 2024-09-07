from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class OperadorEntity(BaseEntity):
    __tablename__ = 'operador'

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_supervisor = db.Column(db.Integer, db.ForeignKey('administrador.id'))

    supervisor = db.relationship('AdministradorEntity', back_populates='operador')

    def __init__(self,
        id_usuario: int = None,
        id_supervisor: int = None
        ) -> None:
        self.id_usuario = id_usuario
        self.id_supervisor = id_supervisor

    def __repr__(self):
        return "<Operador %r>" % self.id
