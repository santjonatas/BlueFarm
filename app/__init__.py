import os
from dotenv import load_dotenv

from flask import Flask
from flask_migrate import Migrate
import pyodbc

from app.application.settings.extensions import db
from app.application.settings.extensions import lm

from app.models.entities.usuario_management.pessoa_entity import PessoaEntity
from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity
from app.models.entities.usuario_management.administrador_entity import AdministradorEntity
from app.models.entities.usuario_management.operador_entity import OperadorEntity

from app.controllers.blueprints.login.login_controller import login_controller_blueprint
from app.controllers.blueprints.registro.registro_operador_controller import registro_operador_controller_blueprint


load_dotenv()


app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

app.config.from_object('config')
db.init_app(app)
lm.init_app(app)


@lm.user_loader
def load_user(user_id):
    return UsuarioEntity.query.get(user_id) 


app.register_blueprint(login_controller_blueprint)
app.register_blueprint(registro_operador_controller_blueprint)


migrate = Migrate(app, db)
