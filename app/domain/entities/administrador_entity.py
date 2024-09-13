from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema

class AdministradorEntity(BaseEntity):
    __tablename__ = 'administradores'

    id_funcionario = db.Column(db.Integer, db.ForeignKey(f'{schema}.funcionarios.id'))
    id_departamento = db.Column(db.Integer, db.ForeignKey(f'{schema}.departamentos.id'))


    funcionario = db.relationship('FuncionarioEntity', uselist=False, back_populates='administrador')
    departamento = db.relationship('DepartamentoEntity', uselist=False, back_populates='administrador')
    operador = db.relationship('OperadorEntity', uselist=False, back_populates='administrador')

    def __init__(self,
        id_funcionario: int,
        id_departamento: int
        ) -> None:
        self.id_funcionario = id_funcionario
        self.id_departamento = id_departamento

    def __repr__(self):
        return "<Administrador %r>" % self.id
