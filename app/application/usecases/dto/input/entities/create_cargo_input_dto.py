class CreateCargoInputDto:
    def __init__(self, id_nivel: int, funcao: str=None, salario: float=None) -> None:
        self.id_nivel = id_nivel
        self.funcao = funcao
        self.salario = salario

    @property
    def to_dict(self) -> dict:
        return {
            'id_nivel': self.id_nivel if self.id_nivel is not None else 0,
            'funcao': self.funcao if self.funcao is not None else '',
            'salario': self.salario if self.salario is not None else ''
        }
