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
from app.exceptions.database.ColheitaEntityException import ColheitaEntityException
from app.exceptions.database.CultivoEntityException import CultivoEntityException
from app.exceptions.database.DepartamentoEntityException import DepartamentoEntityException
from app.infra.services.database.cultivo.cultivo_service import CultivoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService
from app.infra.services.database.estoque.estoque_service import EstoqueService

repositories = GlobalRepositories()
departamento_service = DepartamentoService(departamento_repository=repositories.departamento_repository)

class CreateDepartamentoUseCase:
    def __init__(self
        ) -> None:
        pass

    def execute(self, input_dto: CreateDepartamentoInputDto) -> CreateDepartamentoOutputDto:

        try:
            try:
                departamento_input = CreateDepartamentoInputDto(
                    area=input_dto.area
                )

                departamento_entity =  departamento_service.create(input_dto=departamento_input) 

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise DepartamentoEntityException(str(e))
            
        except DepartamentoEntityException:
            pass
        finally:
            return CreateDepartamentoOutputDto(departamento_entity=departamento_entity)
