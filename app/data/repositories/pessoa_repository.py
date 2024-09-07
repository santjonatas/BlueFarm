from requests import Session
from app.application.contracts.data.repositories.i_pessoa_repository import IPessoaRepository
from app.domain.entities.pessoa_entity import PessoaEntity


class PessoaRepository(IPessoaRepository):
    def __init__(self, session: Session):
        super().__init__(session, PessoaEntity)
