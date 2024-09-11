from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class AdministradorEntity(BaseEntity):
    __tablename__ = 'administrador'

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_departamento = db.Column(db.Integer, db.ForeignKey('departamento.id'))

    departamento = db.relationship('DepartamentoEntity', back_populates='administrador')
    operador = db.relationship('OperadorEntity', uselist=False, back_populates='supervisor')

    def __init__(self,
        id_usuario: int,
        id_departamento: int
        ) -> None:
        self.id_usuario = id_usuario
        self.id_departamento = id_departamento

    def __repr__(self):
        return "<Administrador %r>" % self.id
