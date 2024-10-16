from datetime import datetime
import traceback
from app.application.config.global_repositories import GlobalRepositories
from app.application.usecases.dto.input.entities.create_cultivo_input_dto import CreateCultivoInsumoInputDto
from app.application.usecases.dto.input.produto.create_cultivo_input_dto import CreateCultivoInputDto
from app.application.usecases.dto.out.produto.create_cultivo_output_dto import CreateCultivoOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.database.CultivoEntityException import CultivoEntityException
from app.infra.services.database.cultivo.cultivo_service import CultivoService

repositories = GlobalRepositories()
cultivo_service = CultivoService(cultivo_repository=repositories.cultivo_repository)

class CreateCultivoUseCase:
    def __init__(self
        ) -> None:
        pass

    def execute(self, input_dto: CreateCultivoInputDto) -> CreateCultivoOutputDto:

        insumo_entity = repositories.insumo_repository.get(obj_id=input_dto.id_insumo)
        if insumo_entity.quantidade < input_dto.quantidade:
            raise InvalidFieldException("Quantidade de insumos insuficiente.")

        quantidade_atual_insumo = insumo_entity.quantidade - input_dto.quantidade

        try:
            try:
                cultivo_input = CreateCultivoInsumoInputDto(
                    id_insumo=input_dto.id_insumo,
                    quantidade=input_dto.quantidade,
                    status=input_dto.status,
                    data_inicio=input_dto.data_inicio,
                    data_fim=input_dto.data_fim
                )

                cultivo_entity = cultivo_service.create(input_dto=cultivo_input)

                if input_dto.data_fim == None:
                    repositories.cultivo_repository.atualizar_data_fim(cultivo_id=cultivo_entity.id, nova_data_fim=None)

                repositories.insumo_repository.atualizar_quantidade(insumo_id=input_dto.id_insumo, nova_quantidade=quantidade_atual_insumo)

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise CultivoEntityException(str(e))
            
        except CultivoEntityException:
            pass
        finally:
            return CreateCultivoOutputDto(cultivo_entity=cultivo_entity)
