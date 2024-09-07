from requests import Session
from app.application.contracts.data.repositories.i_funcionario_repository import IFuncionarioRepository
from app.domain.entities.funcionario_entity import FuncionarioEntity


class FuncionarioRepository(IFuncionarioRepository):
    def __init__(self, session: Session):
        super().__init__(session, FuncionarioEntity)
