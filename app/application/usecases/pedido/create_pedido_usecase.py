import traceback
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.application.usecases.dto.input.entities.create_operador_input_dto import CreateOperadorInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.dto.out.pedido.create_pedido_output_dto import CreatePedidoOutputDto
from app.application.usecases.dto.out.users.create_operador_user_output_dto import CreateOperadorUserOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.auth.UserAlreadyExistsException import UserAlreadyExistsException
from app.exceptions.database.OperadorEntityException import OperadorEntityException
from app.exceptions.database.FuncionarioEntityException import FuncionarioEntityException
from app.exceptions.database.PessoaEntityException import PessoaEntityException
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
    
    def execute(self, input_dto: CreatePedidoInputDto) -> CreatePedidoOutputDto:
        # if not self.global_utils.regex_validator_util.verificar_email(email=input_dto.email):
        #     raise InvalidFieldException('Email inválido.')

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
                # raise PessoaEntityException(str(e))

            # try:
            #     usuario_input = CreateUsuarioInputDto(
            #         id_pessoa=pessoa_entity.id,
            #         username=f'{input_dto.username}@op',
            #         senha=input_dto.senha
            #     )

            #     usuario_entity = self.usuario_service.create(input_dto=usuario_input)
            # except Exception as e:
            #     stacktrace = traceback.format_exc()
            #     raise UsuarioEntityException(str(e))

            # try:
            #     funcionario_input = CreateFuncionarioInputDto(
            #         id_usuario=usuario_entity.id,
            #         id_cargo=input_dto.cargo,
            #         data_admissao=input_dto.data_admissao,
            #     )

            #     funcionario_entity = self.funcionario_service.create(input_dto=funcionario_input)
            # except Exception as e:
            #     stacktrace = traceback.format_exc()
            #     raise FuncionarioEntityException(str(e))

            # try:
            #     operador_input = CreateOperadorInputDto(
            #         id_funcionario=funcionario_entity.id,
            #         id_supervisor=input_dto.supervisor
            #     )

            #     operador_entity = self.operador_service.create(input_dto=operador_input)

            #     print('Registrou tudo paizao')
            # except Exception as e:
            #     stacktrace = traceback.format_exc()
            #     raise OperadorEntityException(str(e))
        # except PessoaEntityException:
        #     pass
        # except FuncionarioEntityException:
        #     self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
        # except UsuarioEntityException:
        #     self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
        #     self.funcionario_service.funcionario_repository.delete(funcionario_entity.id)
        # except OperadorEntityException:
        #     self.pessoa_service.pessoa_repository.delete(pessoa_entity.id)
        #     self.funcionario_service.funcionario_repository.delete(funcionario_entity.id)
        #     self.usuario_service.usuario_repository.delete(usuario_entity.id)
        except:
            stacktrace = traceback.format_exc()
        finally:
            return CreatePedidoOutputDto(pedido_entity=pedido_entity)
