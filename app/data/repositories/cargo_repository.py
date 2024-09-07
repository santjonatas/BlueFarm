from requests import Session
from app.application.contracts.data.repositories.i_cargo_repository import ICargoRepository
from app.domain.entities.cargo_entity import CargoEntity


class CargoRepository(ICargoRepository):
    def __init__(self, session: Session):
        super().__init__(session, CargoEntity)
