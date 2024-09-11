from app.application.config.global_services import GlobalServices
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.auth.create_administrador_usecase import CreateAdminUserUseCase


class GlobalUseCases:
    def __init__(self, global_services: GlobalServices, global_utils: GlobalUtils) -> None:
        self.create_admin_user_usecase = CreateAdminUserUseCase(
            pessoa_service=global_services.pessoa_service,
            funcionario_service=global_services.funcionario_service,
            usuario_service=global_services.usuario_service,
            administrador_service=global_services.administrador_service,
            cargo_service=global_services.cargo_service,
            departamento_service=global_services.departamento_service,
            global_utils=global_utils
        )
