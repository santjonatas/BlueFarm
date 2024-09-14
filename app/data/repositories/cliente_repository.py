from requests import Session
from app.application.contracts.data.repositories.i_cliente_repository import IClienteRepository
from app.domain.entities.cliente_entity import ClienteEntity


class ClienteRepository(IClienteRepository):
    def __init__(self, session: Session):
        super().__init__(session, ClienteEntity)
