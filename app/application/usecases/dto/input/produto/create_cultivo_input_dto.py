from datetime import datetime 
from typing import Optional 

class CreateCultivoInputDto: 
    def __init__(self, 
        id_insumo: Optional[int] = None, 
        quantidade: Optional[int] = None, 
        status: Optional[str] = None, 
        data_inicio: Optional[str] = None, 
        data_fim: Optional[str] = None
        ) -> None: 
        
        # Atributos de CreateCultivoInputDto 
        self.id_insumo = id_insumo 
        self.quantidade = quantidade 
        self.status = status 
        self.data_inicio = data_inicio 
        self.data_fim = data_fim 
        