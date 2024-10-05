from app.domain.entities.produto_entity import ProdutoEntity


class CreateProdutoOutputDto:
    def __init__(self, produto_entity: ProdutoEntity) -> None:
        self.produto_entity = produto_entity
