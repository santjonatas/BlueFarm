from requests import Session
from app.application.contracts.data.repositories.i_departamento_repository import IDepartamentoRepository
from app.domain.entities.departamento_entity import DepartamentoEntity


class DepartamentoRepository(IDepartamentoRepository):
    def __init__(self, session: Session):
        super().__init__(session, DepartamentoEntity)

    def get_by_departamento(self, area: str) -> DepartamentoEntity:
        return self.session.query(self.entity).filter(self.entity.area==area).first()

    def exists_by_area(self, area: str) -> bool:
        """Verifica se o departamento fornecido já existe na tabela."""
        departamento = self.session.query(DepartamentoEntity).filter(DepartamentoEntity.area == area).first()
        return departamento is not None