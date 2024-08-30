from app.application.contracts.i_administrador_repository import IAdministradorRepository
from app.models.entities.usuario_management.administrador_entity import AdministradorEntity


class AdministradorRepository(IAdministradorRepository):
    def __init__(self, session):
        super().__init__(session, AdministradorEntity)