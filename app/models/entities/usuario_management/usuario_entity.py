from app.application.settings.extensions import db
from app.models.entities.common.base_entity import BaseEntity

from flask_login import UserMixin

import os
from dotenv import load_dotenv


load_dotenv()

schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')


class UsuarioEntity(BaseEntity, UserMixin):
    __tablename__ = 'usuario'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    id_funcionario = db.Column(db.Integer, db.ForeignKey(f'{schema}.funcionario.id'))
    username = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String, nullable=False)
    permissao = db.Column(db.String(15), nullable=False)

    def __init__(self, 
                 username,
                 senha,
                 permissao = None,
                 id_funcionario = None
                 ) -> None:
        self.username = username
        self.senha = senha
        self.permissao = permissao
        self.id_funcionario = id_funcionario
        super().__init__()
        pass

    def __repr__(self):
        return "<Usuario %r>" % self.username
    
    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return str(self.id)