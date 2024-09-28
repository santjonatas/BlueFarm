from app.application.contracts.data.repositories.i_produto_repository import IProdutoRepository
from app.application.usecases.dto.input.entities.create_produto_input_dto import CreateProdutoInputDto
from app.domain.entities.produto_entity import ProdutoEntity


class ProdutoService:
    def __init__(self, produto_repository: IProdutoRepository) -> None:
        self.produto_repository = produto_repository
    
    def create(self, input_dto: CreateProdutoInputDto) -> ProdutoEntity:
        produto_entity = ProdutoEntity(**input_dto.to_dict)
        return self.produto_repository.add(produto_entity)
