from flask import Flask
from flask_restx import Api

api = Api(prefix='/dev/api/v1/', doc='/dev/api/v1/docs/')


class ApiSetting:
    def __init__(self, app: Flask) -> None:
        api.init_app(app=app)
        api.add_namespace(app.global_apis.auth_endpoint.namespace)
