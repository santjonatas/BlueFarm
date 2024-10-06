from datetime import datetime
from typing import Optional


class CreatePagamentoInputDto:
    def __init__(self,
        id_pedido: Optional[int] = None,
        metodo_pagamento: Optional[str] = None,
        data_pagamento: Optional[str] = None,
        status_pagamento: Optional[str] = None
        ) -> None:
    
        self.id_pedido = id_pedido
        self.metodo_pagamento = metodo_pagamento
        self.data_pagamento = data_pagamento
        self.status_pagamento = status_pagamento

    
    @property
    def to_dict(self) -> dict:
        return {
            'id_pedido': self.id_pedido if self.id_pedido is not None else '',
            'metodo_pagamento': self.metodo_pagamento if self.metodo_pagamento is not None else '',
            'data_pagamento': self.data_pagamento if self.data_pagamento is not None else '',
            'status_pagamento': self.status_pagamento if self.status_pagamento is not None else ''
        }