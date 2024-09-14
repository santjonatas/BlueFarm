from requests import Session
from app.application.contracts.data.repositories.i_produto_repository import IProdutoRepository
from app.domain.entities.produto_entity import ProdutoEntity


class ProdutoRepository(IProdutoRepository):
    def __init__(self, session: Session):
        super().__init__(session, ProdutoEntity)