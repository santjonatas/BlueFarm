from app.application.settings.extensions import db
from app.models.entities.common.base_entity import BaseEntity
import os
from dotenv import load_dotenv


load_dotenv()
schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')


class FuncionarioEntity(BaseEntity):
    __tablename__ = 'funcionario'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    id_pessoa = db.Column(db.Integer, db.ForeignKey(f'{schema}.pessoa.id'))
    data_admissao = db.Column(db.Date, nullable=False)
    cargo = db.Column(db.String(25), nullable=False)
    salario = db.Column(db.Numeric(10, 2), nullable=False)
    data_demissao = db.Column(db.Date, nullable=True)

    def __init__(self, 
                 data_admissao,
                 cargo,
                 salario,
                 data_demissao,
                 id_pessoa = None
                 ) -> None:
        self.data_admissao = data_admissao
        self.cargo = cargo
        self.salario = salario
        self.data_demissao = data_demissao
        self.id_pessoa = id_pessoa
        super().__init__()
        pass

    def __repr__(self):
        return "<Funcionario %r>" % self.id