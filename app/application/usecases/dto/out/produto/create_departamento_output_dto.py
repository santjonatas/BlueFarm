from app.domain.entities.departamento_entity import DepartamentoEntity


class CreateDepartamentoOutputDto:
    def __init__(self, departamento_entity: DepartamentoEntity) -> None:
        self.departamento_entity = departamento_entity
