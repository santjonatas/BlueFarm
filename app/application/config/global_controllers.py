from app.controllers.auth.login_controller import LoginController
from app.controllers.auth.register_controller import RegisterController
from app.controllers.configuracoes.configuracoes_controller import ConfiguracoesController
from app.controllers.controle_producao.controle_producao_controller import ControleProducaoController
from app.controllers.dashboard.dashboard_controller import DashboardController
from app.controllers.gestao_estoque.gestao_estoque_controller import GestaoEstoqueController
from app.controllers.gestao_vendas.gestao_vendas_controller import GestaoVendasController
from app.controllers.home.home_controller import HomeController
from app.controllers.main.main_controller import MainController


class GlobalControllers:
    def __init__(self) -> None:
        self.login_controller = LoginController()
        self.register_controller = RegisterController()
        self.home_controller = HomeController()
        self.main_controller = MainController()
        self.dashboard_controller = DashboardController()
        self.gestao_estoque = GestaoEstoqueController()
        self.gestao_vendas = GestaoVendasController()
        self.controle_producao_controller = ControleProducaoController()
        self.configuracoes_controller = ConfiguracoesController()