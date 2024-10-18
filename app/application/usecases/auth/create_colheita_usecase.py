from datetime import datetime
import traceback
from app.application.config.global_repositories import GlobalRepositories
from app.application.usecases.dto.input.entities.create_colheita_input_dto import CreateColheitaInsumoInputDto
from app.application.usecases.dto.input.entities.create_cultivo_input_dto import CreateCultivoInsumoInputDto
from app.application.usecases.dto.input.produto.create_colheita_input_dto import CreateColheitaInputDto
from app.application.usecases.dto.input.produto.create_cultivo_input_dto import CreateCultivoInputDto
from app.application.usecases.dto.out.produto.create_colheita_output_dto import CreateColheitaOutputDto
from app.application.usecases.dto.out.produto.create_cultivo_output_dto import CreateCultivoOutputDto
from app.exceptions.auth.InvalidFieldException import InvalidFieldException
from app.exceptions.database.ColheitaEntityException import ColheitaEntityException
from app.exceptions.database.CultivoEntityException import CultivoEntityException
from app.infra.services.database.colheita.colheita_service import ColheitaService
from app.infra.services.database.cultivo.cultivo_service import CultivoService
from app.infra.services.database.estoque.estoque_service import EstoqueService

repositories = GlobalRepositories()
colheita_service = ColheitaService(colheita_repository=repositories.colheita_repository)

class CreateColheitaUseCase:
    def __init__(self
        ) -> None:
        pass

    def execute(self, input_dto: CreateColheitaInputDto, cultivo_id: int) -> CreateColheitaOutputDto:

        cultivo_entity = repositories.cultivo_repository.get(obj_id=cultivo_id)

        insumo_entity = repositories.insumo_repository.get(obj_id=cultivo_entity.id_insumo)

        if repositories.produto_repository.exists_by_name(nome=insumo_entity.nome) == False:
            raise InvalidFieldException(f"Produto não encontrado.")

        produto_entity = repositories.produto_repository.get_produto_by_name(nome=insumo_entity.nome)

        try:
            try:
                colheita_input = CreateColheitaInsumoInputDto(
                    id_cultivo=cultivo_entity.id,
                    id_produto=produto_entity.id,
                    quantidade=input_dto.quantidade,
                    data=input_dto.data
                )

                colheita_entity =  colheita_service.create(input_dto=colheita_input) 

                repositories.estoque_repository.incrementar_estoque(id_produto=produto_entity.id, quantidade=input_dto.quantidade)

                repositories.cultivo_repository.atualizar_status_colhido(cultivo_id=cultivo_entity.id)

            except Exception as e:
                stacktrace = traceback.format_exc()
                raise ColheitaEntityException(str(e))
            
        except ColheitaEntityException:
            pass
        finally:
            return CreateColheitaOutputDto(colheita_entity=colheita_entity)
