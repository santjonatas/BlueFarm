from app.application.config.global_services import GlobalServices
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.auth.alter_estoque_insumo_usecase import AlterEstoqueInsumoUseCase
from app.application.usecases.auth.alter_status_pedido_usecase import AlterStatusPedidoUseCase
from app.application.usecases.auth.create_administrador_usecase import CreateAdminUserUseCase
from app.application.usecases.auth.create_cliente_usecase import CreateClienteUserUseCase
from app.application.usecases.auth.create_cultivo_usecase import CreateCultivoUseCase
from app.application.usecases.auth.create_operador_usecase import CreateOperadorUserUseCase
from app.application.usecases.auth.alter_estoque_produto_usecase import AlterEstoqueProdutoUseCase
from app.application.usecases.auth.create_produto_usecase import CreateProdutoUseCase
from app.application.usecases.pedido.create_pagamento_usecase import CreatePagamentoUseCase
from app.application.usecases.pedido.create_pedido_usecase import CreatePedidoUseCase


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

        self.create_pedido_usecase = CreatePedidoUseCase(
            cliente_service = global_services.cliente_service,
            pedido_service = global_services.pedido_service,
            item_pedido_service = global_services.item_pedido_service,
            produto_service = global_services.produto_service,
            estoque_service = global_services.estoque_service
        )

        self.create_produto_usecase = CreateProdutoUseCase(
            produto_service = global_services.produto_service,
            insumo_service = global_services.insumo_service,
            estoque_service = global_services.estoque_service
        )

        self.create_pagamento_usecase = CreatePagamentoUseCase(
            pagamento_service = global_services.pagamento_service
        )

        self.alter_estoque_produto_usecase = AlterEstoqueProdutoUseCase(
            estoque_service = global_services.estoque_service
        )

        self.alter_estoque_insumo_usecase = AlterEstoqueInsumoUseCase(
            insumo_service = global_services.insumo_service
        )

        self.alter_status_pedido_usecase = AlterStatusPedidoUseCase(
            pedido_service = global_services.pedido_service
        )

        self.create_cultivo_usecase = CreateCultivoUseCase(
        )