class CreateDepartamentoInputDto:
    def __init__(self, area: str=None) -> None:
        self.area = area

    @property
    def to_dict(self) -> dict:
        return {
            'area': self.area if self.area is not None else '',
        }
