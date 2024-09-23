from app.application.config.global_repositories import GlobalRepositories
from app.infra.services.database.admin.admin_service import AdministradorService
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.operador.operador_service import OperadorService
from app.infra.services.database.pessoa.pessoa_service import PessoaService
from app.infra.services.database.usuario.usuario_service import UsuarioService


class GlobalServices:
    def __init__(self, global_repositories: GlobalRepositories) -> None:
        self.cargo_service = CargoService(
            cargo_repository=global_repositories.cargo_repository)
        self.departamento_service = DepartamentoService(
            departamento_repository=global_repositories.departamento_repository)
        self.pessoa_service = PessoaService(
            pessoa_repository=global_repositories.pessoa_repository)
        self.funcionario_service = FuncionarioService(
            funcionario_repository=global_repositories.funcionario_repository
        )
        self.usuario_service = UsuarioService(
            usuario_repository=global_repositories.usuario_repository
        )
        self.administrador_service = AdministradorService(
            administrador_repository=global_repositories.administrador_repository
        )
        self.operador_service = OperadorService(
            operador_repository=global_repositories.operador_repository
        )
