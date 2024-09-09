from app.controllers.auth.login_controller import LoginController
from app.controllers.auth.register_controller import RegisterController
from app.controllers.home.home_controller import HomeController


class GlobalControllers:
    def __init__(self) -> None:
        self.login_controller = LoginController()
        self.register_controller = RegisterController()
        self.home_controller = HomeController()

