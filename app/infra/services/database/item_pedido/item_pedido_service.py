from app.application.contracts.data.repositories.i_item_pedido_repository import IItemPedidoRepository
from app.application.usecases.dto.input.entities.create_item_pedido_input_dto import CreateItemPedidoInputDto
from app.domain.entities.item_pedido_entity import ItemPedidoEntity


class ItemPedidoService:
    def __init__(self, item_pedido_repository: IItemPedidoRepository) -> None:
        self.item_pedido_repository = item_pedido_repository
    
    def create(self, input_dto: CreateItemPedidoInputDto) -> ItemPedidoEntity:
        item_pedido_entity = ItemPedidoEntity(**input_dto.to_dict)
        return self.item_pedido_repository.add(item_pedido_entity)
