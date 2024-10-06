from app.application.contracts.data.repositories.i_insumo_repository import IInsumoRepository
from app.application.usecases.dto.input.entities.create_insumo_input_dto import CreateInsumoInputDto
from app.domain.entities.insumo_entity import InsumoEntity


class InsumoService:
    def __init__(self, insumo_repository: IInsumoRepository) -> None:
        self.insumo_repository = insumo_repository
    
    def create(self, input_dto: CreateInsumoInputDto) -> InsumoEntity:
        insumo_entity = InsumoEntity(**input_dto.to_dict)
        return self.insumo_repository.add(insumo_entity)
