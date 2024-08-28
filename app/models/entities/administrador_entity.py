from app.application.settings.extensions import db
from app.models.entities.common.base_entity import BaseEntity
import os
from dotenv import load_dotenv


load_dotenv()
schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')


class AdministradorEntity(BaseEntity):
    __tablename__ = 'administrador'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey(f'{schema}.usuario.id'))
    permissao_adicional = db.Column(db.String(50), nullable=False)
    responsavel_por_departamento = db.Column(db.String(50), nullable=False)

    def __init__(self,
                 permissao_adicional,
                 responsavel_por_departamento
                 ) -> None:
        self.permissao_adicional = permissao_adicional,
        self.responsavel_por_departamento = responsavel_por_departamento,
        super().__init__()
        pass

    def __repr__(self):
        return "<Administrador %r>" % self.id