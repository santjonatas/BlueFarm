from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema

class OperadorEntity(BaseEntity):
    __tablename__ = 'operadores'

    id_funcionario = db.Column(db.Integer, db.ForeignKey(f'{schema}.funcionarios.id'))
    id_supervisor = db.Column(db.Integer, db.ForeignKey(f'{schema}.administradores.id'))

    funcionario = db.relationship('FuncionarioEntity', uselist=False, back_populates='operador')
    administrador = db.relationship('AdministradorEntity', uselist=False, back_populates='operador')

    def __init__(self,
        id_funcionario: int = None,
        id_supervisor: int = None
        ) -> None:
        self.id_funcionario = id_funcionario
        self.id_supervisor = id_supervisor

    def __repr__(self):
        return "<Operador %r>" % self.id
