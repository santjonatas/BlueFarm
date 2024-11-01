from app.domain.entities.cargo_entity import CargoEntity


class CreateCargoOutputDto:
    def __init__(self, cargo_entity: CargoEntity) -> None:
        self.cargo_entity = cargo_entity
