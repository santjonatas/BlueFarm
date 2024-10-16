from app.domain.entities.cultivo_entity import CultivoEntity


class CreateCultivoOutputDto:
    def __init__(self, cultivo_entity: CultivoEntity) -> None:
        self.cultivo_entity = cultivo_entity
