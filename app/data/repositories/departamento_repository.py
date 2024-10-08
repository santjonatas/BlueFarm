from requests import Session
from app.application.contracts.data.repositories.i_departamento_repository import IDepartamentoRepository
from app.domain.entities.departamento_entity import DepartamentoEntity


class DepartamentoRepository(IDepartamentoRepository):
    def __init__(self, session: Session):
        super().__init__(session, DepartamentoEntity)

    def get_by_departamento(self, area: str) -> DepartamentoEntity:
        return self.session.query(self.entity).filter(self.entity.area==area).first()
