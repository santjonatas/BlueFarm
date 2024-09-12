from datetime import datetime
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class PessoaEntity(BaseEntity):
    __tablename__ = 'pessoas'

    # id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text, nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(100), nullable=False, unique=True)
    genero = db.Column(db.String(25), nullable=True)
    telefone = db.Column(db.String(11), nullable=True, unique=True)
    email = db.Column(db.String(100), nullable=True, unique=True)
    endereco = db.Column(db.Text, nullable=True)

    usuario = db.relationship('UsuarioEntity', uselist=False, back_populates='pessoa')

    def __init__(self, 
        nome: str, 
        data_nascimento: datetime, 
        cpf: str, 
        genero: str,
        telefone: str,
        email: str,
        endereco: str
        ) -> None:

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.genero = genero
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def __repr__(self):
        return "<Pessoa %r>" % self.nome
