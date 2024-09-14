from requests import Session
from app.application.contracts.data.repositories.i_insumo_repository import IInsumoRepository
from app.domain.entities.insumo_entity import InsumoEntity


class InsumoRepository(IInsumoRepository):
    def __init__(self, session: Session):
        super().__init__(session, InsumoEntity)
