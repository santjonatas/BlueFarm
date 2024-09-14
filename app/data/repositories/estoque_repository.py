from requests import Session
from app.application.contracts.data.repositories.i_estoque_repository import IEstoqueRepository
from app.domain.entities.estoque_entity import EstoqueEntity


class EstoqueRepository(IEstoqueRepository):
    def __init__(self, session: Session):
        super().__init__(session, EstoqueEntity)
