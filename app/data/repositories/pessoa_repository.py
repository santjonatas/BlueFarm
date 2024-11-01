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
    
    def atualizar_pessoa(self,
        id: int,
        genero: str = None, 
        telefone: str = None, 
        email: str = None, 
        endereco: str = None
    ) -> bool:
        # Busca a pessoa pelo ID
        pessoa = self.session.query(PessoaEntity).filter_by(id=id).first()

        if not pessoa:
            return False  # Se não encontrar, retorna falso ou lida com o erro da forma adequada

        # Atualiza apenas os campos que não são None
        if genero is not None and genero != '':
            pessoa.genero = genero
        if telefone is not None and telefone != '':
            pessoa.telefone = telefone
        if email is not None and email != '':
            pessoa.email = email
        if endereco is not None and endereco != '':
            pessoa.endereco = endereco

        # Faz o commit das alterações no banco
        self.session.commit()
        return True
