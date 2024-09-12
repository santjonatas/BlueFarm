from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class CargoEntity(BaseEntity):
    __tablename__ = 'cargos'

    id = db.Column(db.Integer, primary_key=True)
    id_nivel = db.Column(db.Integer, db.ForeignKey(f'niveis.id'))
    funcao = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Numeric(10, 2), nullable=False)

    funcionarios = db.relationship('FuncionarioEntity', uselist=False, back_populates='cargos')
    niveis = db.relationship('NiveisEntity', uselist=False, back_populates='cargos')

    def __init__(self,
        id_nivel: int,
        funcao: str,
        salario: str) -> None:

        self.id_nivel = id_nivel
        self.funcao = funcao
        self.salario = salario
