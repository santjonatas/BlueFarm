import traceback
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.application.usecases.dto.input.entities.create_item_pedido_input_dto import CreateItemPedidoInputDto
from app.application.usecases.dto.input.entities.create_operador_input_dto import CreateOperadorInputDto
from app.application.usecases.dto.input.entities.create_pagamento_item_input_dto import CreatePagamentoInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.dto.out.pedido.create_pagamento_output_dto import CreatePagamentoOutputDto
from app.application.usecases.dto.out.pedido.create_pedido_output_dto import CreatePedidoOutputDto
from app.application.usecases.dto.out.users.create_operador_user_output_dto import CreateOperadorUserOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.auth.UserAlreadyExistsException import UserAlreadyExistsException
from app.exceptions.database.ItemPedidoEntityException import ItemPedidoEntityException
from app.exceptions.database.OperadorEntityException import OperadorEntityException
from app.exceptions.database.FuncionarioEntityException import FuncionarioEntityException
from app.exceptions.database.PagamentoEntityException import PagamentoEntityException
from app.exceptions.database.PedidoEntityException import PedidoEntityException
from app.exceptions.database.UsuarioEntityException import UsuarioEntityException
from app.infra.services.database.cliente.cliente_service import ClienteService
from app.infra.services.database.estoque.estoque_service import EstoqueService
from app.infra.services.database.item_pedido.item_pedido_service import ItemPedidoService
from app.infra.services.database.operador.operador_service import OperadorService
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.admin.admin_service import AdministradorService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.pagamento.pagamento_service import PagamentoService
from app.infra.services.database.pedido.pedido_service import PedidoService
from app.infra.services.database.pessoa.pessoa_service import PessoaService
from app.infra.services.database.produto.produto_service import ProdutoService
from app.infra.services.database.usuario.usuario_service import UsuarioService
from app.infra.utils.security.crypto_util import CryptoUtil
from app.application.config.global_repositories import GlobalRepositories


repositories = GlobalRepositories()

class CreatePagamentoUseCase:
    def __init__(self,
        pagamento_service: PagamentoService
        ) -> None:
        self.pagamento_service = pagamento_service
    
    def execute(self, input_dto: CreatePagamentoInputDto) -> CreatePagamentoOutputDto:
        if repositories.pagamento_repository.get_pagamento_by_id_pedido(id_pedido=input_dto.id_pedido):
            raise PagamentoEntityException('O pagamento desse pedido já foi realizado.')

        try:
            try:
                pagamento_input = CreatePagamentoInputDto(
                    id_pedido=input_dto.id_pedido,
                    metodo_pagamento=input_dto.metodo_pagamento,
                    data_pagamento=input_dto.data_pagamento,
                    status_pagamento=input_dto.status_pagamento
                )

                pagamento_entity = self.pagamento_service.create(input_dto=pagamento_input)

                repositories.pedido_repository.atualizar_status(id_pedido=input_dto.id_pedido, status='Pago')

                itens_pedido = repositories.item_pedido_repository.get_itens_by_pedido(id_pedido=input_dto.id_pedido)

                for item in itens_pedido:
                    repositories.estoque_repository.decrementar_estoque(
                        id_produto=item.id_produto, 
                        quantidade=item.quantidade
                    )

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise PagamentoEntityException(str(e))
  
        except PagamentoEntityException:
            pass
        except:
            stacktrace = traceback.format_exc()
        finally:
            return CreatePagamentoOutputDto(pagamento_entity=pagamento_entity)
