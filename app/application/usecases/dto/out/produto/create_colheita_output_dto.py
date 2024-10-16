from app.domain.entities.colheita_entity import ColheitaEntity


class CreateColheitaOutputDto:
    def __init__(self, colheita_entity: ColheitaEntity) -> None:
        self.colheita_entity = colheita_entity
