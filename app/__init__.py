from flask import Flask
from flask_migrate import Migrate
import pyodbc

from app.application.settings.extensions import db
from app.models.entities.pessoa_entity import PessoaEntity

import os
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)

app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
