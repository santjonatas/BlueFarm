from datetime import datetime 
from typing import Optional 

class CreateColheitaInputDto: 
    def __init__(self, 
        id_cultivo: Optional[int] = None, 
        id_produto: Optional[int] = None, 
        quantidade: Optional[int] = None, 
        data: Optional[str] = None
        ) -> None: 
        
        # Atributos de CreateColheitaInputDto 
        self.id_cultivo = id_cultivo
        self.id_produto = id_produto 
        self.quantidade = quantidade 
        self.data = data
        
    