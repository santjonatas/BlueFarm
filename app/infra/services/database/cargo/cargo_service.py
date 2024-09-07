from app.application.contracts.data.repositories.i_cargo_repository import ICargoRepository
from app.application.usecases.dto.input.create_cargo_input_dto import CreateCargoInputDto
from app.domain.entities.cargo_entity import CargoEntity

class CargoService:
    def __init__(self, cargo_repository: ICargoRepository):
        self.cargo_repository = cargo_repository

    def create(self, input_dto: CreateCargoInputDto) -> CargoEntity:
        cargo_entity = CargoEntity(**input_dto.to_dict)
        return self.cargo_repository.add(cargo_entity)
