from requests import Session
from app.application.contracts.data.repositories.i_nivel_repository import INivelRepository
from app.domain.entities.nivel_enity import NivelEntity


class NivelRepository(INivelRepository):
    def __init__(self, session: Session):
        super().__init__(session, NivelEntity)