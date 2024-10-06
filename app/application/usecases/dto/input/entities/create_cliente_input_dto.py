class CreateClienteInputDto:
    def __init__(self,
        id_usuario: int,
        status: bool) -> None:
        
        self.id_usuario = id_usuario
        self.status = status
    
    @property
    def to_dict(self) -> dict:
        return {
            'id_usuario': self.id_usuario if self.id_usuario is not None else '',
            'status': self.status if self.status is not None else '',
        }
