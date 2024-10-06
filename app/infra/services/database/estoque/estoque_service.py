from app.application.contracts.data.repositories.i_estoque_repository import IEstoqueRepository
from app.application.usecases.dto.input.entities.create_estoque_input_dto import CreateEstoqueInputDto
from app.domain.entities.estoque_entity import EstoqueEntity


class EstoqueService:
    def __init__(self, estoque_repository: IEstoqueRepository) -> None:
        self.estoque_repository = estoque_repository
    
    def create(self, input_dto: CreateEstoqueInputDto) -> EstoqueEntity:
        estoque_entity = EstoqueEntity(**input_dto.to_dict)
        return self.estoque_repository.add(estoque_entity)
