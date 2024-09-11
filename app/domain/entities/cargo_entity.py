from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class CargoEntity(BaseEntity):
    __tablename__ = 'cargo'

    funcao = db.Column(db.String(50), nullable=False)
    salario = db.Column(db.Numeric(10, 2), nullable=False)

    funcionario = db.relationship('FuncionarioEntity', uselist=False, back_populates='cargo')

    def __init__(self,
        funcao: str,
        salario: str) -> None:

        self.funcao = funcao
        self.salario = salario
