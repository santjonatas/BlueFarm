class CreateAdministradorInputDto:
    def __init__(self,
        id_funcionario: int,
        id_departamento: int) -> None:
        
        self.id_funcionario = id_funcionario
        self.id_departamento = id_departamento
    
    @property
    def to_dict(self) -> dict:
        return {
            'id_funcionario': self.id_funcionario if self.id_funcionario is not None else '',
            'id_departamento': self.id_departamento if self.id_departamento is not None else '',
        }
