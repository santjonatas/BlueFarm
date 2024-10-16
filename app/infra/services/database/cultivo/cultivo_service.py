from app.application.contracts.data.repositories.i_cultivo_repository import ICultivoRepository
from app.application.usecases.dto.input.entities.create_cultivo_input_dto import CreateCultivoInsumoInputDto
from app.application.usecases.dto.input.produto.create_cultivo_input_dto import CreateCultivoInputDto
from app.domain.entities.cultivo_entity import CultivoEntity


class CultivoService:
    def __init__(self, cultivo_repository: ICultivoRepository) -> None:
        self.cultivo_repository = cultivo_repository
    
    def create(self, input_dto: CreateCultivoInputDto) -> CultivoEntity:
        cultivo_entity = CultivoEntity(**input_dto.to_dict)
        return self.cultivo_repository.add(cultivo_entity)
