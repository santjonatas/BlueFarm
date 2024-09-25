from app.application.config.global_services import GlobalServices
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.auth.create_administrador_usecase import CreateAdminUserUseCase
from app.application.usecases.auth.create_cliente_usecase import CreateClienteUserUseCase
from app.application.usecases.auth.create_operador import CreateOperadorUserUseCase


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

        self.create_operador_user_usecase = CreateOperadorUserUseCase(
            pessoa_service=global_services.pessoa_service,
            funcionario_service=global_services.funcionario_service,
            operador_service=global_services.operador_service,
            usuario_service=global_services.usuario_service,
            administrador_service=global_services.administrador_service,
            cargo_service=global_services.cargo_service,
            global_utils=global_utils
        )

        self.create_cliente_user_usecase = CreateClienteUserUseCase(
            pessoa_service=global_services.pessoa_service,
            usuario_service=global_services.usuario_service,
            cliente_service=global_services.cliente_service,
            global_utils=global_utils
        )
