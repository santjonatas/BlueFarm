from datetime import datetime 
from typing import Optional 

class AlterStatusPedidoInputDto: 
    def __init__(self,
        status: Optional[int] = None
        ) -> None: 
        
        # Atributos de CreatePedidoInputDto 
        self.status = status