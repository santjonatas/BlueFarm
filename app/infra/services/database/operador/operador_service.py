from app.application.contracts.data.repositories.i_operador_repository import IOperadorRepository
from app.application.usecases.dto.input.entities.create_operador_input_dto import CreateOperadorInputDto
from app.domain.entities.operador_entity import OperadorEntity


class OperadorService:
    def __init__(self, operador_repository: IOperadorRepository) -> None:
        self.operador_repository = operador_repository
    
    def create(self, input_dto: CreateOperadorInputDto) -> OperadorEntity:
        operador_entity = OperadorEntity(**input_dto.to_dict)
        return self.operador_repository.add(operador_entity)
