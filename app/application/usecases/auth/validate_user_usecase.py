from app.application.config.global_utils import GlobalUtils
from app.application.usecases.dto.input.auth.validate_user_input_dto import ValidateUserInputDto
from app.application.usecases.dto.outputs.auth.validate_user_output_dto import ValidateUserOutputDto
from app.exceptions.auth.UserDoesntExistsException import UserDoesntExistsException
from app.infra.services.database.usuario.usuario_service import UsuarioService


class ValidateUserUseCase:
    def __init__(self,
        global_utils: GlobalUtils,
        usuario_service: UsuarioService) -> None:
        self.global_utils = global_utils
        self.usuario_service = usuario_service
    
    def execute(self, input_dto: ValidateUserInputDto) -> ValidateUserOutputDto:
        usuario_entity = self.usuario_service.usuario_repository.get_by_username(username=input_dto.username)

        if usuario_entity is None:
            raise UserDoesntExistsException('Username inválido.')
        
        if not self.global_utils.pwd_hasher_util.verify_password(
            hashed_password=usuario_entity.senha, password=input_dto.senha):
            raise UserDoesntExistsException('Senha inválida.')

        return ValidateUserOutputDto(usuario=usuario_entity)
