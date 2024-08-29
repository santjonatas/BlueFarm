from app.application.contracts.i_pessoa_repository import IPessoaRepository
from app.models.entities.usuario_management.pessoa_entity import PessoaEntity


class PersonRepository(IPessoaRepository):
    def __init__(self, session):
        super().__init__(session, PessoaEntity)

    def telefone_existe(self, phone: str) -> bool:
        return self.session.query(self.entity).filter(self.entity.phone==phone).first() is not None
