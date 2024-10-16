from datetime import datetime
from typing import Optional


class CreateCultivoInsumoInputDto:
    def __init__(self,
        id_insumo: Optional[int] = None,
        quantidade: Optional[int] = None,
        status: Optional[str] = None,
        data_inicio: Optional[str] = None,
        data_fim: Optional[str] = None
        ) -> None:
    
        self.id_insumo = id_insumo
        self.quantidade = quantidade
        self.status = status
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    
    @property
    def to_dict(self) -> dict:
        return {
            'id_insumo': self.id_insumo if self.id_insumo is not None else 0,
            'quantidade': self.quantidade if self.quantidade is not None else 0,
            'status': self.status if self.status is not None else '',
            'data_inicio': self.data_inicio if self.data_inicio is not None else '',
            'data_fim': self.data_fim if self.data_fim is not None else ''
        }