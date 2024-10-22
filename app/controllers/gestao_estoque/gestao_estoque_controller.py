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
from app.application.usecases.auth.create_produto_usecase import CreateProdutoUseCase
from app.application.usecases.dto.input.entities.create_estoque_input_dto import CreateEstoqueInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_produto_input_dto import CreateProdutoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_insumo_input_dto import AlterEstoqueInsumoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_produto_input_dto import AlterEstoqueProdutoInputDto
from app.application.usecases.dto.input.produto.create_produto_item_input_dto import CreateProdutoItemInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.pedido.create_pedido_usecase import CreatePedidoUseCase
from app.domain.forms.add_produto import AddProdutoForm
from flask_wtf import FlaskForm

from app.domain.forms.editar_insumo import EditarInsumoForm
from app.domain.forms.editar_produto import EditarProdutoForm

repositories = GlobalRepositories()

class GestaoEstoqueController:
    def __init__(self):
        self.blueprint = Blueprint('gestao_estoque', __name__)
        self.register_routes()

    def register_routes(self): 
        self.blueprint.add_url_rule('/estoque_insumos/', view_func=self.estoque_insumos, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/editar_insumo/', view_func=self.editar_insumo, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/alterar_estoque_insumo/<int:insumo_id>', view_func=self.alterar_estoque_insumo, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/movimentacao_estoque/', view_func=self.movimentacao_estoque, methods=['GET', 'POST'])

    @login_required
    def estoque_insumos(self) -> None:
        if '@adm' in current_user.username or '@op' in current_user.username: 
            insumo_entity = repositories.insumo_repository.list()
            
            return render_template(
                'gestao_estoque/estoque_insumos.html',
                insumos=insumo_entity, 
                repositories=repositories
                )
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401

    @login_required
    def editar_insumo(self) -> None:
        if '@adm' in current_user.username or '@op' in current_user.username: 
            insumo_id = request.form.get('insumo_id')
            insumo_nome = request.form.get('insumo_nome')
            insumo_preco = request.form.get('insumo_preco')
            insumo_quantidade = request.form.get('insumo_quantidade')
            
            form: FlaskForm = EditarInsumoForm()

            return render_template('gestao_estoque/editar_estoque_insumo.html', form=form, insumo_nome=insumo_nome, insumo_quantidade=insumo_quantidade, insumo_id=insumo_id)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401


    @login_required
    def alterar_estoque_insumo(self, insumo_id):
        if '@adm' in current_user.username or '@op' in current_user.username: 
            form: FlaskForm = EditarInsumoForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    
                    input_dto = AlterEstoqueInsumoInputDto(**form.to_dict())

                    usecase: AlterEstoqueInsumoUseCase = current_app.global_usecases.alter_estoque_insumo_usecase

                    insumo_entity = usecase.execute(input_dto=input_dto, insumo_id=insumo_id)

                    flash(message='Estoque Alterado', category='info')

                    return redirect(url_for('gestao_estoque.estoque_insumos'))

                    pass
                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Alterar Quantidade', category='info')
                    pass

            return redirect(url_for('gestao_estoque.estoque_insumos'))
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
    
    @login_required
    def movimentacao_estoque(self) -> None:
        if '@adm' in current_user.username or '@op' in current_user.username: 
            pedido_entity = repositories.pedido_repository.obter_pedidos_pagos_hoje()
            
            return render_template(
                'gestao_estoque/movimentacao_estoque.html',
                pedidos_hoje=pedido_entity
                )
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
        