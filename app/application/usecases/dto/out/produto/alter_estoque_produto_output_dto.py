from app.domain.entities.estoque_entity import EstoqueEntity


class AlterEstoqueProdutoOutputDto:
    def __init__(self, estoque_entity: EstoqueEntity) -> None:
        self.estoque_entity = estoque_entity
