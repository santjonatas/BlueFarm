from app.application.settings.extensions_setting import db
from app.data.repositories.admistrador_repository import AdministradorRepository
from app.data.repositories.cargo_repository import CargoRepository
from app.data.repositories.departamento_repository import DepartamentoRepository
from app.data.repositories.funcionario_repository import FuncionarioRepository
from app.data.repositories.nivel_repository import NivelRepository
from app.data.repositories.pessoa_repository import PessoaRepository
from app.data.repositories.usuario_repository import UsuarioRepository

class GlobalRepositories:
    def __init__(self) -> None:
        session = db.session

        self.cargo_repository = CargoRepository(session=session)
        self.departamento_repository = DepartamentoRepository(session=session)
        self.pessoa_repository = PessoaRepository(session=session)
        self.funcionario_repository = FuncionarioRepository(session=session)
        self.usuario_repository = UsuarioRepository(session=session)
        self.administrador_repository = AdministradorRepository(session=session)
        self.nivel_repository = NivelRepository(session=session)