from app.application.settings.extensions import db
from app.models.entities.common.base_entity import BaseEntity
import os
from dotenv import load_dotenv


load_dotenv()
schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA')


class OperadorEntity(BaseEntity):
    __tablename__ = 'operador'
    __table_args__ = {'schema': schema}

    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey(f'{schema}.usuario.id'))
    area_operacao = db.Column(db.String(50), nullable=False)
    supervisor_direto = db.Column(db.String(50), nullable=True)

    def __init__(self,
                 area_operacao,
                 supervisor_direto,
                 id_usuario = None
                 ) -> None:
        self.area_operacao = area_operacao
        self.supervisor_direto = supervisor_direto
        self.id_usuario = id_usuario
        super().__init__()
        pass

    def __repr__(self):
        return "<Operador %r>" % self.id