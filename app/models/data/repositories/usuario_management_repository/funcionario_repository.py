from app.application.contracts.i_funcionario_repository import IFuncionarioRepository
from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity


class FuncionarioRepository(IFuncionarioRepository):
    def __init__(self, session):
        super().__init__(session, FuncionarioEntity)