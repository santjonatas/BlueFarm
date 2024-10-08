from datetime import datetime 
from typing import Optional 

class AlterEstoqueProdutoInputDto: 
    def __init__(self,
        quantidade_disponivel: Optional[int] = None
        ) -> None: 
        
        # Atributos de CreateEstoqueInputDto 
        self.quantidade_disponivel = quantidade_disponivel