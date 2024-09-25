from app.domain.entities.cliente_entity import ClienteEntity


class CreateClienteUserOutputDto:
    def __init__(self, cliente_entity: ClienteEntity) -> None:
        self.cliente_entity = cliente_entity
