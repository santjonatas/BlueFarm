import traceback
from flask_login import login_user, logout_user
from flask_restx import Resource, Namespace
from flask import current_app, request
from app.api.v1.swagger.auth.login_model import LoginModel
from app.api.v1.swagger.auth.register_model import RegisterModel
from app.api.v1.swagger.common.error_model import ErrorModel
from app.application.usecases.auth.create_administrador_usecase import CreateAdminUserUseCase
from app.application.usecases.auth.validate_user_usecase import ValidateUserUseCase
from app.application.usecases.dto.input.auth.validate_user_input_dto import ValidateUserInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.exceptions.auth.BadRequestException import BadRequestException
from app.exceptions.auth.ValidationException import ValidationException
from app.exceptions.database.DatabaseException import DatabaseException

namespace = Namespace('security/auth', "Endpoints de autenticação")


class AuthEndpoint:
    def __init__(self) -> None:
        self.namespace = namespace
        self.register_routes()

    def register_routes(self) -> None:
        self.namespace.add_resource(self.LoginResource, '/login')
        self.namespace.add_resource(self.LogoutResource, '/logout')
        self.namespace.add_resource(self.RegisterAdminResource, '/register_admin')

    class LoginResource(Resource):
        @namespace.doc("Loga um usuário no sistema")
        @namespace.expect(LoginModel.login_input())
        @namespace.response(200, 'OK', LoginModel.login_output())
        @namespace.response(400, 'Bad Request', ErrorModel.error_model())
        @namespace.response(404, 'Not Found', ErrorModel.error_model())
        @namespace.response(500, 'Internal Server Error', ErrorModel.error_model())
        def post(self) -> tuple[dict, int]:
            data = request.json

            try:
                try:
                    input_dto = ValidateUserInputDto(**data)
                except Exception as e:
                    raise BadRequestException('Dados fornecidos são inválidos.')

                usecase = ValidateUserUseCase(
                    global_utils=current_app.global_utils,
                    usuario_service=current_app.global_services.usuario_service)
                output_dto = usecase.execute(input_dto=input_dto)
                login_user(user=output_dto.usuario)

                return ({
                    'success': True,
                    'statuscode': 200,
                    'message': 'Usuário logado com sucesso.'
                }, 200)

            except BadRequestException as bde:
                stacktrace = traceback.format_exc()
                return ({
                    'success': False,
                    'message': str(bde),
                    'details': stacktrace,
                    'statuscode': 400}, 400)

            except ValidationException as ve:
                stacktrace = traceback.format_exc()
                return ({
                    'success': False,
                    'message': str(ve),
                    'details': stacktrace,
                    'statuscode': 404}, 404)

            except Exception as e:
                stacktrace = traceback.format_exc()
                return ({
                    'success': False,
                    'message': str(e),
                    'details': stacktrace,
                    'statuscode': 500}, 500)

    class LogoutResource(Resource):
        @namespace.response(200, 'OK', LoginModel.logout_output())
        def post(self) -> None:
            logout_user()
            return ({
                'success': True,
                'statuscode': 200,
                'message': 'Usuário deslogado com sucesso.'
            }, 201)

    class RegisterAdminResource(Resource):
        @namespace.doc("Loga um usuário no sistema")
        @namespace.expect(RegisterModel.register_input())
        @namespace.response(200, 'OK', RegisterModel.register_output())
        @namespace.response(400, 'Bad Request', ErrorModel.error_model())
        @namespace.response(404, 'Not Found', ErrorModel.error_model())
        @namespace.response(500, 'Internal Server Error', ErrorModel.error_model())
        def post(self) -> tuple[dict, int]:
            data = request.json

            try:
                try:
                    input_dto = CreateAdminUserInputDto(**data)
                except Exception as e:
                    raise BadRequestException('Dados fornecidos são inválidos.')
                
                usecase = CreateAdminUserUseCase(
                    pessoa_service=current_app.global_services.pessoa_service,
                    funcionario_service=current_app.global_services.funcionario_service,
                    administrador_service=current_app.global_services.administrador_service,
                    usuario_service=current_app.global_services.usuario_service,
                    cargo_service=current_app.global_services.cargo_service,
                    departamento_service=current_app.global_services.departamento_service,
                    global_utils=current_app.global_utils
                )
                usecase.execute(input_dto=input_dto)

                return ({
                    'success': True,
                    'statuscode': 201,
                    'message': 'Administrador registrado com sucesso.'
                }, 201)
            
            except BadRequestException as bde:
                stacktrace = traceback.format_exc()
                return ({
                    'success': False,
                    'message': str(bde),
                    'details': stacktrace,
                    'statuscode': 400}, 400)

            except DatabaseException as de:
                stacktrace = traceback.format_exc()
                return ({
                    'success': False,
                    'message': str(de),
                    'details': stacktrace,
                    'statuscode': 500}, 500)

            except ValidationException as ve:
                stacktrace = traceback.format_exc()
                return ({
                    'success': False,
                    'message': str(ve),
                    'details': stacktrace,
                    'statuscode': 404}, 404)

            except Exception as e:
                stacktrace = traceback.format_exc()
                return ({
                    'success': False,
                    'message': str(e),
                    'details': stacktrace,
                    'statuscode': 500}, 500)
