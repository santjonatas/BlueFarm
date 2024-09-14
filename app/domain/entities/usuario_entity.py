from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class UsuarioEntity(BaseEntity, UserMixin):
    __tablename__ = 'usuarios'

    id_pessoa = db.Column(db.Integer, db.ForeignKey(f'{schema}.pessoas.id'))
    username = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String, nullable=False)

    pessoa = db.relationship('PessoaEntity', uselist=False, back_populates='usuario')
    funcionario = db.relationship('FuncionarioEntity', uselist=False, back_populates='usuario')
    cliente = db.relationship('ClienteEntity', uselist=False, back_populates='usuario')

    def __init__(self, 
        id_pessoa: int,
        username: str,
        senha: str
        ) -> None:
        self.id_pessoa = id_pessoa
        self.username = username
        self.senha = senha

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
