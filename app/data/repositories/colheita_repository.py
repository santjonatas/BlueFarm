from requests import Session
from app.application.contracts.data.repositories.i_colheita_repository import IColheitaRepository
from app.domain.entities.colheita_entity import ColheitaEntity


class ColheitaRepository(IColheitaRepository):
    def __init__(self, session: Session):
        super().__init__(session, ColheitaEntity)
