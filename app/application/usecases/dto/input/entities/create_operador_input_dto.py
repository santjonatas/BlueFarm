class CreateOperadorInputDto:
    def __init__(self,
        id_funcionario: int,
        id_supervisor: int) -> None:
        
        self.id_funcionario = id_funcionario
        self.id_supervisor = id_supervisor
    
    @property
    def to_dict(self) -> dict:
        return {
            'id_funcionario': self.id_funcionario if self.id_funcionario is not None else '',
            'id_supervisor': self.id_supervisor if self.id_supervisor is not None else '',
        }
