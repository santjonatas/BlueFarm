from app.application.settings.extensions import db
import os
from dotenv import load_dotenv


load_dotenv()
schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')


class UsuarioEntity(db.Model):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    id_funcionario = db.Column(db.Integer, db.ForeignKey(f'{schema}.funcionario.id'))
    username = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String, nullable=False)

    def __init__(self, 
                 username,
                 senha
                 ) -> None:
        self.username = username
        self.senha = senha
        super().__init__()
        pass

    def __repr__(self):
        return "<Usuario %r>" % self.username