from datetime import datetime
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity


class FuncionarioEntity(BaseEntity):
    __tablename__ = 'funcionario'

    id_usuario = db.Column(db.Integer, db.ForeignKey('pessoa.id'))
    id_cargo = db.Column(db.Integer, db.ForeignKey('cargo.id'))
    data_admissao = db.Column(db.Date, nullable=False)

    usuario = db.relationship('UsuarioEntity', back_populates='funcionario')
    cargo = db.relationship('CargoEntity', back_populates='funcionario')

    def __init__(self, 
        data_admissao: datetime,
        id_cargo: int = None,
        id_pessoa: int = None
        ) -> None:

        self.data_admissao = data_admissao
        self.id_cargo = id_cargo
        self.id_pessoa = id_pessoa

    def __repr__(self):
        return "<Funcionario %r>" % self.id
