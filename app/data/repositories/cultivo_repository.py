from requests import Session
from app.application.contracts.data.repositories.i_cultivo_repository import ICultivoRepository
from app.domain.entities.cultivo_entity import CultivoEntity


class CultivoRepository(ICultivoRepository):
    def __init__(self, session: Session):
        super().__init__(session, CultivoEntity)
