from app.controllers.auth.login_controller import LoginController
from app.controllers.auth.register_controller import RegisterController


class GlobalControllers:
    def __init__(self) -> None:
        self.login_controller = LoginController()
        self.register_controller = RegisterController()
