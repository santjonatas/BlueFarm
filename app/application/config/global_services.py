from app.application.config.global_repositories import GlobalRepositories
from app.infra.services.cohere_ia.cohere_ia_service import CohereIaService
from app.infra.services.database.admin.admin_service import AdministradorService
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.cliente.cliente_service import ClienteService
from app.infra.services.database.colheita.colheita_service import ColheitaService
from app.infra.services.database.cultivo.cultivo_service import CultivoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService
from app.infra.services.database.estoque.estoque_service import EstoqueService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.insumo.insumo_service import InsumoService
from app.infra.services.database.item_pedido.item_pedido_service import ItemPedidoService
from app.infra.services.database.operador.operador_service import OperadorService
from app.infra.services.database.pagamento.pagamento_service import PagamentoService
from app.infra.services.database.pedido.pedido_service import PedidoService
from app.infra.services.database.pessoa.pessoa_service import PessoaService
from app.infra.services.database.produto.produto_service import ProdutoService
from app.infra.services.database.usuario.usuario_service import UsuarioService


class GlobalServices:
    def __init__(self, global_repositories: GlobalRepositories) -> None:
        self.cargo_service = CargoService(
            cargo_repository=global_repositories.cargo_repository
        )
        self.departamento_service = DepartamentoService(
            departamento_repository=global_repositories.departamento_repository
        )
        self.pessoa_service = PessoaService(
            pessoa_repository=global_repositories.pessoa_repository
        )
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
        self.cliente_service = ClienteService(
            cliente_repository=global_repositories.cliente_repository
        )
        self.pedido_service = PedidoService(
            pedido_repository=global_repositories.pedido_repository
        )
        self.item_pedido_service = ItemPedidoService(
            item_pedido_repository=global_repositories.item_pedido_repository
        )
        self.produto_service = ProdutoService(
            produto_repository=global_repositories.produto_repository
        )
        self.estoque_service = EstoqueService(
            estoque_repository=global_repositories.estoque_repository
        )
        self.insumo_service = InsumoService(
            insumo_repository=global_repositories.insumo_repository
        )
        self.pagamento_service = PagamentoService(
            pagamento_repository=global_repositories.pagamento_repository
        )
        self.cultivo_service = CultivoService(
            cultivo_repository=global_repositories.cultivo_repository
        )
        self.cohere_ia_service = CohereIaService(

        )
        self.colheita_service = ColheitaService(
            colheita_repository=global_repositories.colheita_repository
        )