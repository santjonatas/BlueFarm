from app.application.contracts.i_pessoa_repository import IPessoaRepository
from app.models.entities.usuario_management.pessoa_entity import PessoaEntity


class PessoaRepository(IPessoaRepository):
    def __init__(self, session):
        super().__init__(session, PessoaEntity)

    def telefone_existe(self, telefone: str) -> bool:
        return self.session.query(self.entity).filter(self.entity.telefone==telefone).first() is not None
    
    def obter_email(self, email: str) -> PessoaEntity:
        return self.session.query(self.entity).filter(self.entity.email==email).first()

    def email_existe(self, email: str) -> bool:
        return self.get_by_email(email=email) is not None
