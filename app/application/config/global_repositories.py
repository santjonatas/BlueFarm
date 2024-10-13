from app.application.settings.extensions_setting import db
from app.data.repositories.admistrador_repository import AdministradorRepository
from app.data.repositories.cargo_repository import CargoRepository
from app.data.repositories.cliente_repository import ClienteRepository
from app.data.repositories.cultivo_repository import CultivoRepository
from app.data.repositories.departamento_repository import DepartamentoRepository
from app.data.repositories.estoque_repository import EstoqueRepository
from app.data.repositories.funcionario_repository import FuncionarioRepository
from app.data.repositories.insumo_repository import InsumoRepository
from app.data.repositories.item_pedido_repository import ItemPedidoRepository
from app.data.repositories.nivel_repository import NivelRepository
from app.data.repositories.operador_repository import OperadorRepository
from app.data.repositories.pagamento_repository import PagamentoRepository
from app.data.repositories.pedido_repository import PedidoRepository
from app.data.repositories.pessoa_repository import PessoaRepository
from app.data.repositories.produto_repository import ProdutoRepository
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
        self.operador_repository = OperadorRepository(session=session)
        self.cliente_repository = ClienteRepository(session=session)
        self.produto_repository = ProdutoRepository(session=session)
        self.pedido_repository = PedidoRepository(session=session)
        self.item_pedido_repository = ItemPedidoRepository(session=session)
        self.estoque_repository = EstoqueRepository(session=session)
        self.insumo_repository = InsumoRepository(session=session)
        self.pagamento_repository = PagamentoRepository(session=session)
        self.cultivo_repository = CultivoRepository(session=session)