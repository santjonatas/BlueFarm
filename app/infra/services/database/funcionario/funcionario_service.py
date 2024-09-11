from app.application.contracts.data.repositories.i_funcionario_repository import IFuncionarioRepository
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.domain.entities.funcionario_entity import FuncionarioEntity


class FuncionarioService:
    def __init__(self, funcionario_repository: IFuncionarioRepository) -> None:
        self.funcionario_repository = funcionario_repository
    
    def create(self, input_dto: CreateFuncionarioInputDto) -> FuncionarioEntity:
        funcionario_entity = FuncionarioEntity(**input_dto.to_dict)
        return self.funcionario_repository.add(funcionario_entity)
