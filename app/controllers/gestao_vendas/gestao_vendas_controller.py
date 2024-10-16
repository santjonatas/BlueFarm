from datetime import datetime
import os
from pprint import pprint
import traceback
from flask import current_app, flash, render_template, redirect, url_for, jsonify, request, session, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from decimal import Decimal
from werkzeug.utils import secure_filename

from app.application.config.global_repositories import GlobalRepositories
from app.application.usecases.auth.alter_estoque_insumo_usecase import AlterEstoqueInsumoUseCase
from app.application.usecases.auth.alter_estoque_produto_usecase import AlterEstoqueProdutoUseCase
from app.application.usecases.auth.alter_status_pedido_usecase import AlterStatusPedidoUseCase
from app.application.usecases.auth.create_produto_usecase import CreateProdutoUseCase
from app.application.usecases.dto.input.entities.create_estoque_input_dto import CreateEstoqueInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_produto_input_dto import CreateProdutoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_insumo_input_dto import AlterEstoqueInsumoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_produto_input_dto import AlterEstoqueProdutoInputDto
from app.application.usecases.dto.input.produto.alter_status_pedido_input_dto import AlterStatusPedidoInputDto
from app.application.usecases.dto.input.produto.create_produto_item_input_dto import CreateProdutoItemInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.pedido.create_pedido_usecase import CreatePedidoUseCase
from app.domain.forms.add_produto import AddProdutoForm
from flask_wtf import FlaskForm

from app.domain.forms.editar_insumo import EditarInsumoForm
from app.domain.forms.editar_pedido import EditarPedidoForm
from app.domain.forms.editar_produto import EditarProdutoForm

repositories = GlobalRepositories()

class GestaoVendasController:
    def __init__(self):
        self.blueprint = Blueprint('gestao_vendas', __name__)
        self.register_routes()

    def register_routes(self): 
        self.blueprint.add_url_rule('/registro_vendas/', view_func=self.registro_vendas, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/editar_venda/', view_func=self.editar_venda, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/alterar_status_venda/<int:pedido_id>', view_func=self.alterar_status_venda, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/lista_clientes/', view_func=self.lista_clientes, methods=['GET', 'POST'])

    @login_required
    def registro_vendas(self) -> None:
        
        pedido_entity = repositories.pedido_repository.obter_pedidos_nao_aguardando_pagamento()
        
        return render_template(
            'gestao_vendas/registro_vendas.html',
            vendas=pedido_entity
            )

    @login_required
    def editar_venda(self) -> None:
        pedido_id = request.form.get('pedido_id')
        pedido_status = request.form.get('pedido_status')
        pedido_valor_total = request.form.get('pedido_valor_total')

        pedido_entity = repositories.pedido_repository.get(obj_id=pedido_id)
        
        form: FlaskForm = EditarPedidoForm()

        return render_template('gestao_vendas/editar_venda.html', 
            form=form, 
            pedido_id=pedido_id, 
            pedido_status=pedido_status, 
            pedido_valor_total=pedido_valor_total, 
            pedido=pedido_entity, 
            repositories=repositories)

    @login_required
    def alterar_status_venda(self, pedido_id):
        form: FlaskForm = EditarPedidoForm()
        print(form.status.data) 

        if form.validate_on_submit():
            try:
                pprint(form.to_dict())
                
                input_dto = AlterStatusPedidoInputDto(**form.to_dict())

                usecase: AlterStatusPedidoUseCase = current_app.global_usecases.alter_status_pedido_usecase

                pedido_entity = usecase.execute(input_dto=input_dto, pedido_id=pedido_id)

                flash(message='Status Alterado', category='info')

                return redirect(url_for('gestao_vendas.registro_vendas'))

                pass
            except Exception as e:
                stacktrace = traceback.format_exc()
                flash(message='Erro ao Alterar Quantidade', category='info')
                pass

        return redirect(url_for('gestao_vendas.registro_vendas'))
    
    @login_required
    def lista_clientes(self) -> None:
        
        cliente_entity = repositories.cliente_repository.list()
        
        return render_template(
            'gestao_vendas/lista_clientes.html',
            clientes=cliente_entity,
            repositories=repositories
            )