from app.application.contracts.i_operador_repository import IOperadorRepository
from app.models.entities.usuario_management.operador_entity import OperadorEntity


class AdministradorRepository(IOperadorRepository):
    def __init__(self, session):
        super().__init__(session, OperadorEntity)