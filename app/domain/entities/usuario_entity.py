from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity

class UsuarioEntity(BaseEntity, UserMixin):
    __tablename__ = 'usuario'

    id_pessoa = db.Column(db.Integer, db.ForeignKey(f'pessoa.id'))
    username = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String, nullable=False)

    
    pessoa = db.relationship('PessoaEntity', back_populates='usuario')
    funcionario = db.relationship('FuncionarioEntity', uselist=False, back_populates='usuario')

    def __init__(self, 
        username: str,
        senha: str,
        id_funcionario: int = None
        ) -> None:
        self.username = username
        self.senha = senha
        self.id_funcionario = id_funcionario

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
