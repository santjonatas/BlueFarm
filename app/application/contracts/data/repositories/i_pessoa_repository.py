from abc import ABC
from app.data.repositories.common.base_repository import BaseRepository
from app.domain.entities.pessoa_entity import PessoaEntity


class IPessoaRepository(ABC, BaseRepository[PessoaEntity]):
    def get_by_cpf(self, cpf: str) -> PessoaEntity:
        ...
    
    def cpf_exists(self, cpf: str) -> bool:
        ...

    def get_by_email(self, email: str) -> PessoaEntity:
        ...
    
    def email_exists(self, email: str) -> bool:
        ...
    
    def get_by_phone_number(self, phone_number: str) -> PessoaEntity:
        ...
    
    def phone_number_exists(self, phone_number: str) -> bool:
        ...
