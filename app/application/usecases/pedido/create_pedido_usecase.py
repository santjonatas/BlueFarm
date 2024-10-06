import traceback
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.application.usecases.dto.input.entities.create_item_pedido_input_dto import CreateItemPedidoInputDto
from app.application.usecases.dto.input.entities.create_operador_input_dto import CreateOperadorInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.dto.out.pedido.create_pedido_output_dto import CreatePedidoOutputDto
from app.application.usecases.dto.out.users.create_operador_user_output_dto import CreateOperadorUserOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.auth.UserAlreadyExistsException import UserAlreadyExistsException
from app.exceptions.database.ItemPedidoEntityException import ItemPedidoEntityException
from app.exceptions.database.OperadorEntityException import OperadorEntityException
from app.exceptions.database.FuncionarioEntityException import FuncionarioEntityException
from app.exceptions.database.PedidoEntityException import PedidoEntityException
from app.exceptions.database.UsuarioEntityException import UsuarioEntityException
from app.infra.services.database.cliente.cliente_service import ClienteService
from app.infra.services.database.estoque.estoque_service import EstoqueService
from app.infra.services.database.item_pedido.item_pedido_service import ItemPedidoService
from app.infra.services.database.operador.operador_service import OperadorService
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.admin.admin_service import AdministradorService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.pedido.pedido_service import PedidoService
from app.infra.services.database.pessoa.pessoa_service import PessoaService
from app.infra.services.database.produto.produto_service import ProdutoService
from app.infra.services.database.usuario.usuario_service import UsuarioService
from app.infra.utils.security.crypto_util import CryptoUtil
from app.application.config.global_repositories import GlobalRepositories

repositories = GlobalRepositories()

class CreatePedidoUseCase:
    def __init__(self,
        cliente_service: ClienteService,
        pedido_service: PedidoService,
        item_pedido_service: ItemPedidoService,
        produto_service: ProdutoService,
        estoque_service: EstoqueService
        ) -> None:
        self.cliente_service = cliente_service
        self.pedido_service = pedido_service
        self.item_pedido_service = item_pedido_service
        self.produto_service = produto_service
        self.estoque_service = estoque_service
    
    def execute(self, input_dto: CreatePedidoInputDto, list_carrinho: list) -> CreatePedidoOutputDto:
        if not list_carrinho:
            raise PedidoEntityException('O seu carrinho não pode estar vazio.')

        try:
            try:
                pedido_input = CreatePedidoInputDto(
                    id_cliente = input_dto.id_cliente,
                    data_pedido = input_dto.data_pedido,
                    status = input_dto.status,
                    valor_total = input_dto.valor_total
                )

                pedido_entity = self.pedido_service.create(input_dto=pedido_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise PedidoEntityException(str(e))

            try:
                for item_produto in list_carrinho:
                    print(item_produto)

                    item_pedido_input = CreateItemPedidoInputDto(
                        id_pedido = pedido_entity.id,
                        id_produto = item_produto['id'],
                        quantidade = item_produto['quantidade'],
                        preco_unitario = item_produto['preco']
                    )

                    item_pedido_entity = self.item_pedido_service.create(input_dto=item_pedido_input)

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise ItemPedidoEntityException(str(e))
                pass
            
        except PedidoEntityException:
            pass
        except ItemPedidoEntityException:
            self.pedido_service.pedido_repository.delete(pedido_entity.id)
        except:
            stacktrace = traceback.format_exc()
        finally:
            return CreatePedidoOutputDto(pedido_entity=pedido_entity)
