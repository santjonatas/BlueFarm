import traceback
from requests import Session
from app.application.contracts.data.repositories.i_cargo_repository import ICargoRepository
from app.domain.entities.cargo_entity import CargoEntity


class CargoRepository(ICargoRepository):
    def __init__(self, session: Session):
        super().__init__(session, CargoEntity)

    def get_by_funcao(self, funcao: str) -> CargoEntity:
        return self.session.query(self.entity).filter(self.entity.funcao==funcao).first()
    
    def exists_by_funcao(self, nome: str) -> bool:
        """Verifica se o cargo com o nome fornecido já existe na tabela."""
        cargo = self.session.query(CargoEntity).filter(CargoEntity.funcao == nome).first()
        return cargo is not None
