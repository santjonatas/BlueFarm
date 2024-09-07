class CreateCargoInputDto:
    def __init__(self, funcao: str=None, salario: float=None) -> None:
        self.funcao = funcao
        self.salario = salario

    @property
    def to_dict(self) -> dict:
        return {
            'funcao': self.funcao if self.funcao is not None else '',
            'salario': self.salario if self.salario is not None else ''
        }
