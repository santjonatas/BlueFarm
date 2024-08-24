from app.application.settings.extensions import db

import os
from dotenv import load_dotenv


load_dotenv()

schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')


class PessoaEntity(db.Model):
    __tablename__ = 'pessoa'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)

    def __init__(self, nome, data_nascimento, cpf) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        super().__init__()

    def __repr__(self):
        return "<Pessoa %r>" % self.nome