from flask_login import UserMixin
from app.application.settings.extensions_setting import db
from app.domain.entities.common.base_entity import BaseEntity, schema


class PagamentoEntity(BaseEntity, UserMixin):
    __tablename__ = 'pagamentos'

    id_pedido = db.Column(db.Integer, db.ForeignKey(f'{schema}.pedidos.id'))
    metodo_pagamento = db.Column(db.String(20), nullable=False)
    data_pagamento = db.Column(db.DateTime, nullable=False)
    status_pagamento = db.Column(db.String(20), nullable=False)


    pedido = db.relationship('PedidoEntity', uselist=False, back_populates='pagamento')

    def __init__(self, 
        id_pedido: int,
        metodo_pagamento: str,
        data_pagamento: str,
        status_pagamento: str
        ) -> None:
        self.id_pedido = id_pedido
        self.metodo_pagamento = metodo_pagamento
        self.data_pagamento = data_pagamento
        self.status_pagamento = status_pagamento

    def __repr__(self):
        return "<Pagamento %r>" % self.id_pedido
        
        
