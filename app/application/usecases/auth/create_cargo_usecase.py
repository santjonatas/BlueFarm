from datetime import datetime
import traceback
from app.application.config.global_repositories import GlobalRepositories
from app.application.usecases.dto.input.entities.create_cargo_input_dto import CreateCargoInputDto
from app.application.usecases.dto.input.entities.create_colheita_input_dto import CreateColheitaInsumoInputDto
from app.application.usecases.dto.input.entities.create_cultivo_input_dto import CreateCultivoInsumoInputDto
from app.application.usecases.dto.input.entities.create_departamento_input_dto import CreateDepartamentoInputDto
from app.application.usecases.dto.input.produto.create_colheita_input_dto import CreateColheitaInputDto
from app.application.usecases.dto.input.produto.create_cultivo_input_dto import CreateCultivoInputDto
from app.application.usecases.dto.out.produto.create_cargo_output_dto import CreateCargoOutputDto
from app.application.usecases.dto.out.produto.create_colheita_output_dto import CreateColheitaOutputDto
from app.application.usecases.dto.out.produto.create_cultivo_output_dto import CreateCultivoOutputDto
from app.application.usecases.dto.out.produto.create_departamento_output_dto import CreateDepartamentoOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.database.CargoEntityException import CargoEntityException
from app.exceptions.database.ColheitaEntityException import ColheitaEntityException
from app.exceptions.database.CultivoEntityException import CultivoEntityException
from app.exceptions.database.DepartamentoEntityException import DepartamentoEntityException
from app.infra.services.database.cargo.cargo_service import CargoService
from app.infra.services.database.cultivo.cultivo_service import CultivoService
from app.infra.services.database.departamento.departamento_service import DepartamentoService
from app.infra.services.database.estoque.estoque_service import EstoqueService

repositories = GlobalRepositories()
cargo_service = CargoService(cargo_repository=repositories.cargo_repository)

class CreateCargoUseCase:
    def __init__(self
        ) -> None:
        pass

    def execute(self, input_dto: CreateCargoInputDto) -> CreateCargoOutputDto:

        if repositories.cargo_repository.exists_by_funcao(nome=input_dto.funcao) == True:
            raise InvalidFieldException("Função já cadastrada.")

        try:
            if input_dto.id_nivel == False:
                input_dto.id_nivel = 2

            try:
                cargo_input = CreateCargoInputDto(
                    id_nivel=input_dto.id_nivel,
                    funcao=input_dto.funcao,
                    salario=input_dto.salario
                )

                cargo_entity =  cargo_service.create(input_dto=cargo_input) 

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise CargoEntityException(str(e))
            
        except CargoEntityException:
            pass
        finally:
            return CreateCargoOutputDto(cargo_entity=cargo_entity)
