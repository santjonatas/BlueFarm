from flask_restx import fields
from app.application.settings.api_setting import api

class RegisterModel:
    @staticmethod
    def register_input() -> any:
        return api.model('Register Admin Model', {
            'nome': fields.String(required=True, description='Nome do administrador'),
            'data_nascimento': fields.DateTime(required=False, description='Data de nascimento do administrador'),
            'cpf': fields.String(required=False, description='CPF do administrador'),
            'genero': fields.String(required=False, description='Gênero do administrador'),
            'telefone': fields.String(required=False, description='Telefone do administrador'),
            'email': fields.String(required=False, description='Email do administrador'),
            'endereco': fields.String(required=False, description='Endereço do administrador'),
            'data_admissao': fields.DateTime(required=False, description='Data de admissão do administrador'),
            'cargo': fields.Integer(required=False, description='Cargo do administrador'),
            'username': fields.String(required=False, description='Nome de usuário do administrador'),
            'senha': fields.String(required=False, description='Senha do administrador'),
            'departamento': fields.Integer(required=False, description='Departamento do administrador')
        })

    @staticmethod
    def register_output() -> any:
        return api.model('Register Output', {
            'success': fields.Boolean,
            'statuscode': fields.Integer(default=201),
            'message': fields.String
        })