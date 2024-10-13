from datetime import datetime
import os
from pprint import pprint
import traceback
from flask import current_app, flash, render_template, redirect, url_for, jsonify, request, session, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from decimal import Decimal
from werkzeug.utils import secure_filename

from app.application.config.global_repositories import GlobalRepositories
from app.application.usecases.auth.alter_estoque_produto_usecase import AlterEstoqueProdutoUseCase
from app.application.usecases.auth.create_cultivo_usecase import CreateCultivoUseCase
from app.application.usecases.auth.create_produto_usecase import CreateProdutoUseCase
from app.application.usecases.dto.input.entities.create_estoque_input_dto import CreateEstoqueInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_produto_input_dto import CreateProdutoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_produto_input_dto import AlterEstoqueProdutoInputDto
from app.application.usecases.dto.input.produto.create_cultivo_input_dto import CreateCultivoInputDto
from app.application.usecases.dto.input.produto.create_produto_item_input_dto import CreateProdutoItemInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.pedido.create_pedido_usecase import CreatePedidoUseCase
from app.domain.forms.add_cultivo import AddCultivoForm
from app.domain.forms.add_produto import AddProdutoForm
from flask_wtf import FlaskForm

from app.domain.forms.editar_produto import EditarProdutoForm

import json
import os
from dotenv import load_dotenv


load_dotenv()

repositories = GlobalRepositories()

class ControleProducaoController:
    def __init__(self):
        self.blueprint = Blueprint('controle_producao', __name__)
        self.register_routes()

    def register_routes(self): 
        self.blueprint.add_url_rule('/irrigacao/', view_func=self.irrigacao, methods=['GET', 'POST'])
        

    @login_required
    def irrigacao(self) -> None:

        json_irrigacao = os.getenv('JSON_IRRIGACAO')

        with open(json_irrigacao, 'r', encoding='utf-8') as arquivo:
            dados_irrigacao = json.load(arquivo)
        
        return render_template(
            'controle_producao/irrigacao.html'
            )
    
    