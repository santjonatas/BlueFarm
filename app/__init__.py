import os
from dotenv import load_dotenv

from flask import Flask
from flask_migrate import Migrate
import pyodbc

from app.application.settings.extensions import db
from app.models.entities.pessoa_entity import PessoaEntity
from app.models.entities.funcionario_entity import FuncionarioEntity
from app.models.entities.usuario_entity import UsuarioEntity
from app.models.entities.administrador_entity import AdministradorEntity
from app.models.entities.operador_entity import OperadorEntity

from app.controllers.blueprints.login.login import login_blueprint


load_dotenv()


app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

app.register_blueprint(login_blueprint)

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
