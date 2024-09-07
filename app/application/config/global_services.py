from app.application.config.global_repositories import GlobalRepositories
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService


class GlobalServices:
    def __init__(self, global_repositories: GlobalRepositories) -> None:
        self.cargo_service = CargoService(
            cargo_repository=global_repositories.cargo_repository)
        self.departamento_service = DepartamentoService(
            departamento_repository=global_repositories.departamento_repository)
