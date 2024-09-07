from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.output.users.create_admin_user_output_dto import CreateAdminUserOutputDto
from app.infra.services.database.admin.admin_service import AdminService
from app.infra.services.database.funcionario.funcionario_service import FuncionarioService
from app.infra.services.database.pessoa.pessoa_service import PessoaService


class CreateAdminUserUseCase:
    def __init__(self,
        pessoa_service: PessoaService,
        funcionario_service: FuncionarioService,
        administrador_service: AdminService) -> None:
        self.pessoa_service = pessoa_service
        self.funcionario_service = funcionario_service
        self.administrador_service = administrador_service

    def execute(self, input_dto: CreateAdminUserInputDto) -> CreateAdminUserOutputDto:
        ...
