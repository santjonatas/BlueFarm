from app.application.contracts.data.repositories.i_cliente_repository import IClienteRepository
from app.application.usecases.dto.input.entities.create_cliente_input_dto import CreateClienteInputDto
from app.domain.entities.cliente_entity import ClienteEntity


class ClienteService:
    def __init__(self, cliente_repository: IClienteRepository) -> None:
        self.cliente_repository = cliente_repository
    
    def create(self, input_dto: CreateClienteInputDto) -> ClienteEntity:
        cliente_entity = ClienteEntity(**input_dto.to_dict)
        return self.cliente_repository.add(cliente_entity)
