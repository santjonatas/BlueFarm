from requests import Session
from app.application.contracts.data.repositories.i_operador_repository import IOperadorRepository
from app.domain.entities.operador_entity import OperadorEntity


class OperadorRepository(IOperadorRepository):
    def __init__(self, session: Session):
        super().__init__(session, OperadorEntity)
