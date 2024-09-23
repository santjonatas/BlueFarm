from app.domain.entities.operador_entity import OperadorEntity


class CreateOperadorUserOutputDto:
    def __init__(self, operador_entity: OperadorEntity) -> None:
        self.operador_entity = operador_entity
