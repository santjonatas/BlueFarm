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
from app.application.usecases.auth.create_produto_usecase import CreateProdutoUseCase
from app.application.usecases.dto.input.entities.create_estoque_input_dto import CreateEstoqueInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_produto_input_dto import CreateProdutoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_produto_input_dto import AlterEstoqueProdutoInputDto
from app.application.usecases.dto.input.produto.create_produto_item_input_dto import CreateProdutoItemInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.pedido.create_pedido_usecase import CreatePedidoUseCase
from app.domain.forms.add_produto import AddProdutoForm
from flask_wtf import FlaskForm

from app.domain.forms.editar_produto import EditarProdutoForm

repositories = GlobalRepositories()

class GestaoEstoqueController:
    def __init__(self):
        self.blueprint = Blueprint('gestao_estoque', __name__)
        self.register_routes()

    def register_routes(self): 
        self.blueprint.add_url_rule('/estoque_insumos/', view_func=self.estoque_insumos, methods=['GET', 'POST'])
        
    @login_required
    def estoque_insumos(self) -> None:
        
        insumo_entity = repositories.insumo_repository.list()
        
        return render_template(
            'gestao_estoque/estoque_insumos.html',
            insumos=insumo_entity, 
            repositories=repositories
            )
    