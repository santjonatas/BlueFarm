from flask_restx import fields
from app.application.settings.api_setting import api

class LoginModel:
    @staticmethod
    def login_input() -> any:
        return api.model('Login Input', {
            'username': fields.String(required=True, description='Nome de usuário'),
            'senha': fields.String(required=True, description='A senha do usuário')
        })

    @staticmethod
    def login_output() -> any:
        return api.model('Login Output', {
            'success': fields.Boolean,
            'statuscode': fields.Integer(default=200),
            'message': fields.String
        })

    @staticmethod
    def logout_output() -> any:
        return api.model('Logout Output', {
            'success': fields.Boolean,
            'statuscode': fields.Integer(default=200),
            'message': fields.String
        })
