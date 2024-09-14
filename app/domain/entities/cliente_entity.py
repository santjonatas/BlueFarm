from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class ClienteEntity(BaseEntity, UserMixin):
    __tablename__ = 'clientes'

    id_usuario = db.Column(db.Integer, db.ForeignKey(f'{schema}.usuarios.id'))
    status = db.Column(db.Boolean, nullable=False, default=False)


    usuario = db.relationship('UsuarioEntity', uselist=False, back_populates='cliente')
    pedido = db.relationship('PedidoEntity', back_populates='cliente')

    def __init__(self, 
        id_usuario: int,
        status: bool
        ) -> None:
        self.id_usuario = id_usuario
        self.status = status

    def __repr__(self):
        return "<Cliente %r>" % self.id_usuario
