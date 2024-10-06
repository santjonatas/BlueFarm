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
from app.application.usecases.dto.input.produto.create_produto_item_input_dto import CreateProdutoItemInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
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

class CreateProdutoUseCase:
    def __init__(self,
        produto_service: ProdutoService,
        insumo_service: InsumoService,
        estoque_service: EstoqueService) -> None:
        self.produto_service = produto_service
        self.insumo_service = insumo_service
        self.estoque_service = estoque_service

    def execute(self, input_dto: CreateProdutoItemInputDto) -> CreateProdutoOutputDto:
        if repositories.produto_repository.exists_by_name(nome=input_dto.nome) == True:
            raise ProdutoEntityException('Produto já existe.')

        try:
            try:
                produto_input = CreateProdutoInputDto(
                    nome=input_dto.nome,
                    descricao=input_dto.descricao,
                    preco=input_dto.preco
                )

                produto_entity = self.produto_service.create(input_dto=produto_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise ProdutoEntityException(str(e))

            try:
                insumo_input = CreateInsumoInputDto(
                    nome=input_dto.nome_insumo,
                    descricao=input_dto.descricao_insumo,
                    preco=input_dto.preco_insumo,
                    comprado_em=input_dto.comprado_em,
                    quantidade=input_dto.quantidade_disponivel_insumo
                )

                insumo_entity = self.insumo_service.create(input_dto=insumo_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise InsumoEntityException(str(e))

            try:
                estoque_input = CreateEstoqueInputDto(
                    id_produto=produto_entity.id,
                    quantidade_disponivel=input_dto.quantidade_disponivel,
                    ultima_atualizacao=datetime.now()
                )

                estoque_entity = self.estoque_service.create(input_dto=estoque_input)
            except Exception as e:
                stacktrace = traceback.format_exc()
                raise EstoqueEntityException(str(e))
            
        except ProdutoEntityException:
            pass
        except InsumoEntityException:
            self.produto_service.produto_repository.delete(produto_entity.id)
        except EstoqueEntityException:
            self.produto_service.produto_repository.delete(produto_entity.id)
            self.insumo_service.insumo_repository.delete(insumo_entity.id)
        finally:
            return CreateProdutoOutputDto(produto_entity=produto_entity)
