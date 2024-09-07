from requests import Session
from app.application.contracts.data.repositories.i_administrador_repository import IAdministradorRepository
from app.domain.entities.administrador_entity import AdministradorEntity


class AdministradorRepository(IAdministradorRepository):
    def __init__(self, session: Session):
        super().__init__(session, AdministradorEntity)
