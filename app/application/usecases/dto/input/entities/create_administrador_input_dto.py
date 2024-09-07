class CreateAdministradorInputDto:
    def __init__(self,
        id_usuario: int,
        id_departamento: int) -> None:
        
        self.id_usuario = id_usuario
        self.id_departamento = id_departamento
    
    @property
    def to_dict(self) -> dict:
        return {
            'id_usuario': self.id_usuario if self.id_usuario is not None else '',
            'id_departamento': self.id_departamento if self.id_departamento is not None else '',
        }
