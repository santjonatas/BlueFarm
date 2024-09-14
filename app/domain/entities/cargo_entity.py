from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema

class CargoEntity(BaseEntity):
    __tablename__ = 'cargos'

    id_nivel = db.Column(db.Integer, db.ForeignKey(f'{schema}.niveis.id'))
    funcao = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.DECIMAL(10, 2), nullable=False)


    funcionario = db.relationship('FuncionarioEntity', uselist=False, back_populates='cargo')
    nivel = db.relationship('NivelEntity', back_populates='cargo')

    def __init__(self,
        id_nivel: int,
        funcao: str,
        salario: float
        ) -> None:
        self.id_nivel = id_nivel
        self.funcao = funcao
        self.salario = salario

    def __repr__(self):
        return "<Cargo %r>" % self.funcao