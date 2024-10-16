from app.domain.entities.insumo_entity import InsumoEntity


class AlterEstoqueInsumoOutputDto:
    def __init__(self, insumo_entity: InsumoEntity) -> None:
        self.insumo_entity = insumo_entity
