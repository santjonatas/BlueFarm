from app.application.contracts.data.repositories.i_colheita_repository import IColheitaRepository
from app.application.usecases.dto.input.entities.create_colheita_input_dto import CreateColheitaInsumoInputDto
from app.application.usecases.dto.input.produto.create_colheita_input_dto import CreateColheitaInputDto
from app.domain.entities.colheita_entity import ColheitaEntity


class ColheitaService:
    def __init__(self, colheita_repository: IColheitaRepository) -> None:
        self.colheita_repository = colheita_repository
    
    def create(self, input_dto: CreateColheitaInputDto) -> ColheitaEntity:
        colheita_entity = ColheitaEntity(**input_dto.to_dict)
        return self.colheita_repository.add(colheita_entity)
