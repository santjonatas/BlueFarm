from datetime import datetime 
from typing import Optional 

class CreateDepartamentoInputDto: 
    def __init__(self, 
        area: Optional[str] = None
        ) -> None: 
        
        # Atributos de CreateDepartamentoInputDto 
        self.area = area
