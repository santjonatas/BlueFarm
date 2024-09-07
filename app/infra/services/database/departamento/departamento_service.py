from app.application.contracts.data.repositories.i_departamento_repository import IDepartamentoRepository
from app.application.usecases.dto.input.create_departamento_input_dto import CreateDepartamentoInputDto
from app.domain.entities import DepartamentoEntity

class DepartamentoService:
    def __init__(self, departamento_repository: IDepartamentoRepository):
        self.departamento_repository = departamento_repository

    def create(self, input_dto: CreateDepartamentoInputDto) -> DepartamentoEntity:
        cargo_entity = DepartamentoEntity(**input_dto.to_dict)
        return self.departamento_repository.add(cargo_entity)
