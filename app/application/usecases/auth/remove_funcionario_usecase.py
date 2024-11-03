from datetime import datetime
import traceback
from app.application.config.global_repositories import GlobalRepositories
from app.application.usecases.dto.input.entities.create_colheita_input_dto import CreateColheitaInsumoInputDto
from app.application.usecases.dto.input.entities.create_cultivo_input_dto import CreateCultivoInsumoInputDto
from app.application.usecases.dto.input.entities.create_departamento_input_dto import CreateDepartamentoInputDto
from app.application.usecases.dto.input.produto.create_colheita_input_dto import CreateColheitaInputDto
from app.application.usecases.dto.input.produto.create_cultivo_input_dto import CreateCultivoInputDto
from app.application.usecases.dto.out.produto.create_colheita_output_dto import CreateColheitaOutputDto
from app.application.usecases.dto.out.produto.create_cultivo_output_dto import CreateCultivoOutputDto
from app.application.usecases.dto.out.produto.create_departamento_output_dto import CreateDepartamentoOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.database.AdministradorEntityException import AdministradorEntityException
from app.exceptions.database.ColheitaEntityException import ColheitaEntityException
from app.exceptions.database.CultivoEntityException import CultivoEntityException
from app.exceptions.database.DepartamentoEntityException import DepartamentoEntityException
from app.exceptions.database.FuncionarioEntityException import FuncionarioEntityException
from app.exceptions.database.OperadorEntityException import OperadorEntityException
from app.exceptions.database.PessoaEntityException import PessoaEntityException
from app.exceptions.database.UsuarioEntityException import UsuarioEntityException
from app.infra.services.database.cultivo.cultivo_service import CultivoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService
from app.infra.services.database.estoque.estoque_service import EstoqueService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService

repositories = GlobalRepositories()
funcionario_service = FuncionarioService(funcionario_repository=repositories.funcionario_repository)

class RemoveFuncionarioUseCase:
    def __init__(self
        ) -> None:
        pass

    def execute(self, id_funcionario) -> bool:

        if not repositories.funcionario_repository.get(obj_id=id_funcionario):
            raise InvalidFieldException("Funcionário não existe")

        try:
            funcionario_entity = repositories.funcionario_repository.get(obj_id=id_funcionario)

            usuario_entity = repositories.usuario_repository.get(obj_id=funcionario_entity.id_usuario)

            pessoa_entity = repositories.pessoa_repository.get(obj_id=usuario_entity.id_pessoa)

            try:
                pessoa_entity_id = pessoa_entity.id
                repositories.pessoa_repository.delete(obj_id=pessoa_entity.id)

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise PessoaEntityException(str(e))
            
            try:
                usuario_entity = repositories.usuario_repository.get(obj_id=usuario_entity.id)

                usuario_entity_id = usuario_entity.id
                usuario_entity_username = usuario_entity.username
                repositories.usuario_repository.delete(obj_id=usuario_entity.id)

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise UsuarioEntityException(str(e))

            try:
                funcionario_entity = repositories.funcionario_repository.get(obj_id=funcionario_entity.id)

                funcionario_entity_id = funcionario_entity.id
                repositories.funcionario_repository.delete(obj_id=funcionario_entity.id)

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise FuncionarioEntityException(str(e))
            
            if '@adm' in usuario_entity_username:
                try:
                    repositories.administrador_repository.deletar_administrador_por_id_funcionario(id_funcionario=funcionario_entity_id)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    raise AdministradorEntityException(str(e))

            if '@op' in usuario_entity_username:
                try:
                    repositories.operador_repository.deletar_operador_por_id_funcionario(id_funcionario=funcionario_entity_id)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    raise OperadorEntityException(str(e))
            
        except PessoaEntityException:
            pass
        except UsuarioEntityException:
            pass
        except FuncionarioEntityException:
            pass
        except AdministradorEntityException:
            pass
        except OperadorEntityException:
            pass
        except Exception as e:
            return False
        finally:
            return True
