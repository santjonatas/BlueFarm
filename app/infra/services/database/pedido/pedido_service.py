from app.application.contracts.data.repositories.i_pedido_repository import IPedidoRepository
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.domain.entities.pedido_entity import PedidoEntity


class PedidoService:
    def __init__(self, pedido_repository: IPedidoRepository) -> None:
        self.pedido_repository = pedido_repository
    
    def create(self, input_dto: CreatePedidoInputDto) -> PedidoEntity:
        pedido_entity = PedidoEntity(**input_dto.to_dict)
        return self.pedido_repository.add(pedido_entity)
