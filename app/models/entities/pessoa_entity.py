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
    cpf = db.Column(db.String(11), nullable=False, unique=True)
    genero = db.Column(db.String(25), nullable=True)
    telefone = db.Column(db.String(11), nullable=True, unique=True)
    email = db.Column(db.String(100), nullable=True, unique=True)
    endereco = db.Column(db.Text, nullable=True)

    def __init__(self, 
                 nome, 
                 data_nascimento, 
                 cpf, 
                 genero,
                 telefone,
                 email,
                 endereco
                 ) -> None:
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        super().__init__()
        pass

    def __repr__(self):
        return "<Pessoa %r>" % self.nome