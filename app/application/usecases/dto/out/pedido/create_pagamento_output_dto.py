from app.domain.entities.pagamento_entity import PagamentoEntity


class CreatePagamentoOutputDto:
    def __init__(self, pagamento_entity: PagamentoEntity) -> None:

        self.pagamento_entity = pagamento_entity
