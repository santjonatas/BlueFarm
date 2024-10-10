from datetime import datetime
import traceback
from app.application.config.global_repositories import GlobalRepositories
from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.entities.create_administrador_input_dto import CreateAdministradorInputDto
from app.application.usecases.dto.input.entities.create_estoque_input_dto import CreateEstoqueInputDto
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.application.usecases.dto.input.entities.create_insumo_input_dto import CreateInsumoInputDto
from app.application.usecases.dto.input.entities.create_pessoa_input_dto import CreatePessoaInputDto
from app.application.usecases.dto.input.entities.create_produto_input_dto import CreateProdutoInputDto
from app.application.usecases.dto.input.entities.create_usuario_input_dto import CreateUsuarioInputDto
from app.application.usecases.dto.input.produto.alter_estoque_insumo_input_dto import AlterEstoqueInsumoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_produto_input_dto import AlterEstoqueProdutoInputDto
from app.application.usecases.dto.input.produto.create_produto_item_input_dto import CreateProdutoItemInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.out.produto.alter_estoque_insumo_output_dto import AlterEstoqueInsumoOutputDto
from app.application.usecases.dto.out.produto.alter_estoque_produto_output_dto import AlterEstoqueProdutoOutputDto
from app.application.usecases.dto.out.produto.create_produto_output_dto import CreateProdutoOutputDto
from app.application.usecases.dto.out.users.create_admin_user_output_dto import CreateAdminUserOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.auth.UserAlreadyExistsException import UserAlreadyExistsException
from app.exceptions.database.AdministradorEntityException import AdministradorEntityException
from app.exceptions.database.EstoqueEntityException import EstoqueEntityException
from app.exceptions.database.FuncionarioEntityException import FuncionarioEntityException
from app.exceptions.database.InsumoEntityException import InsumoEntityException
from app.exceptions.database.PessoaEntityException import PessoaEntityException
from app.exceptions.database.ProdutoEntityException import ProdutoEntityException
from app.exceptions.database.UsuarioEntityException import UsuarioEntityException
from app.infra.services.database.admin.admin_service import AdministradorService
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService
from app.infra.services.database.estoque.estoque_service import EstoqueService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.insumo.insumo_service import InsumoService
from app.infra.services.database.produto.produto_service import ProdutoService
from app.infra.services.database.usuario.usuario_service import UsuarioService
from app.infra.utils.security.crypto_util import CryptoUtil

repositories = GlobalRepositories()

class AlterEstoqueInsumoUseCase:
    def __init__(self,
        insumo_service: InsumoService) -> None:
        self.insumo_service = insumo_service

    def execute(self, input_dto: AlterEstoqueInsumoInputDto, insumo_id) -> AlterEstoqueInsumoOutputDto:

        try:

            try:

                insumo_entity = repositories.insumo_repository.atualizar_quantidade(insumo_id=insumo_id, nova_quantidade=input_dto.quantidade_disponivel)

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise InsumoEntityException(str(e))
            
        except InsumoEntityException:
            pass
        finally:
            return AlterEstoqueInsumoOutputDto(insumo_entity=insumo_entity)
