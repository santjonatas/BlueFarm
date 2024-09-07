from app.application.settings.extensions_setting import db
from app.data.repositories.cargo_repository import CargoRepository
from app.data.repositories.departamento_repository import DepartamentoRepository

class GlobalRepositories:
    def __init__(self) -> None:
        session = db.session

        self.cargo_repository = CargoRepository(session=session)
        self.departamento_repository = DepartamentoRepository(session=session)
