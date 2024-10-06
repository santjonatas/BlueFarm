from app.application.contracts.data.repositories.i_pagamento_repository import IPagamentoRepository
from app.application.usecases.dto.input.entities.create_pagamento_item_input_dto import CreatePagamentoInputDto
from app.domain.entities.pagamento_entity import PagamentoEntity


class PagamentoService:
    def __init__(self, pagamento_repository: IPagamentoRepository) -> None:
        self.pagamento_repository = pagamento_repository
    
    def create(self, input_dto: CreatePagamentoInputDto) -> PagamentoEntity:
        pagamento_entity = PagamentoEntity(**input_dto.to_dict)
        return self.pagamento_repository.add(pagamento_entity)
