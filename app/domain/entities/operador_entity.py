from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class OperadorEntity(BaseEntity):
    __tablename__ = 'operadores'

    id = db.Column(db.Integer, primary_key=True)
    id_funcionario = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    id_supervisor = db.Column(db.Integer, db.ForeignKey('administradores.id'))

    funcionarios = db.relationship('FuncionarioEntity', uselist=False, back_populates='operadores')
    supervisor = db.relationship('AdministradorEntity', uselist=False, back_populates='operadores')

    def __init__(self,
        id_usuario: int = None,
        id_supervisor: int = None
        ) -> None:
        self.id_funcionario = id_usuario
        self.id_supervisor = id_supervisor

    def __repr__(self):
        return "<Operador %r>" % self.id
