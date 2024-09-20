from requests import Session
from app.application.contracts.data.repositories.i_pessoa_repository import IPessoaRepository
from app.domain.entities.pessoa_entity import PessoaEntity
from app.infra.utils.security.crypto_util import CryptoUtil


class PessoaRepository(IPessoaRepository):
    def __init__(self, session: Session):
        super().__init__(session, PessoaEntity)

    def get_by_cpf(self, cpf: str) -> PessoaEntity:
        return self.session.query(self.entity).filter(self.entity.cpf==cpf).first()
    
    def cpf_exists(self, cpf: str) -> bool:
        return self.get_by_cpf(cpf=cpf) is not None

    def get_by_email(self, email: str) -> PessoaEntity:
        return self.session.query(self.entity).filter(self.entity.email==email).first()
    
    def email_exists(self, email: str) -> bool:
        return self.get_by_email(email=email) is not None
    
    def get_by_phone_number(self, phone_number: str) -> PessoaEntity:
        return self.session.query(self.entity).filter(self.entity.telefone==phone_number).first()
    
    def phone_number_exists(self, phone_number: str) -> bool:
        return self.get_by_phone_number(phone_number=phone_number) is not None
