from app.application.contracts.data.repositories.i_administrador_repository import IAdministradorRepository
from app.application.usecases.dto.input.entities.create_administrador_input_dto import CreateAdministradorInputDto
from app.domain.entities.administrador_entity import AdministradorEntity


class AdministradorService:
    def __init__(self, administrador_repository: IAdministradorRepository) -> None:
        self.administrador_repository = administrador_repository
    
    def create(self, input_dto: CreateAdministradorInputDto) -> AdministradorEntity:
        administrador_entity = AdministradorEntity(**input_dto.to_dict)
        return self.administrador_repository.add(administrador_entity)
