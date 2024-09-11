from app.application.contracts.data.repositories.i_usuario_repository import IUsuarioRepository
from app.application.usecases.dto.input.entities.create_funcionario_input_dto import CreateFuncionarioInputDto
from app.domain.entities.funcionario_entity import FuncionarioEntity
from app.domain.entities.usuario_entity import UsuarioEntity


class UsuarioService:
    def __init__(self, usuario_repository: IUsuarioRepository) -> None:
        self.usuario_repository = usuario_repository
    
    def create(self, input_dto: CreateFuncionarioInputDto) -> UsuarioEntity:
        usuario_entity = UsuarioEntity(**input_dto.to_dict)
        return self.usuario_repository.add(usuario_entity)
