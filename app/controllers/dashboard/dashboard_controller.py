from datetime import datetime
import os
from pprint import pprint
import re
import traceback
from flask import current_app, flash, get_flashed_messages, render_template, redirect, url_for, jsonify, request, session, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from decimal import Decimal
from werkzeug.utils import secure_filename
import json

from app.application.config.global_repositories import GlobalRepositories
from app.application.config.global_services import GlobalServices
from app.application.usecases.auth.alter_estoque_produto_usecase import AlterEstoqueProdutoUseCase
from app.application.usecases.auth.create_colheita_usecase import CreateColheitaUseCase
from app.application.usecases.auth.create_cultivo_usecase import CreateCultivoUseCase
from app.application.usecases.auth.create_produto_usecase import CreateProdutoUseCase
from app.application.usecases.dto.input.entities.create_estoque_input_dto import CreateEstoqueInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.entities.create_produto_input_dto import CreateProdutoInputDto
from app.application.usecases.dto.input.produto.alter_estoque_produto_input_dto import AlterEstoqueProdutoInputDto
from app.application.usecases.dto.input.produto.create_colheita_input_dto import CreateColheitaInputDto
from app.application.usecases.dto.input.produto.create_cultivo_input_dto import CreateCultivoInputDto
from app.application.usecases.dto.input.produto.create_produto_item_input_dto import CreateProdutoItemInputDto
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.pedido.create_pedido_usecase import CreatePedidoUseCase
from app.domain.forms.add_colheita import AddColheitaForm
from app.domain.forms.add_cultivo import AddCultivoForm
from app.domain.forms.add_produto import AddProdutoForm
from flask_wtf import FlaskForm

from app.domain.forms.buscar_alimento import BuscarAlimentoForm
from app.domain.forms.editar_produto import EditarProdutoForm

repositories = GlobalRepositories()
services = GlobalServices(global_repositories=repositories)

class DashboardController:
    def __init__(self):
        self.blueprint = Blueprint('dashboard', __name__)
        self.register_routes()

    def register_routes(self): 
        self.blueprint.add_url_rule('/estoque_produtos/', view_func=self.estoque_produtos, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/editar_produto/', view_func=self.editar_produto, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/add_produto/', view_func=self.add_produto, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/alterar_estoque/<int:produto_id>', view_func=self.alterar_estoque, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/cultivo/', view_func=self.cultivo, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/add_cultivo/', view_func=self.add_cultivo, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/buscar_alimentos/', view_func=self.buscar_alimentos, methods=['GET', 'POST'])
        

    @login_required
    def estoque_produtos(self) -> None:
        if '@adm' in current_user.username or '@op' in current_user.username: 
            messages = get_flashed_messages()
            produto_entity = repositories.produto_repository.list()
            
            pedidos_entity = repositories.pedido_repository.list()
            
            return render_template(
                'dashboard/estoque_produtos.html',
                produtos=produto_entity, 
                pedidos=pedidos_entity,
                repositories=repositories
                )
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
    
    @login_required
    def editar_produto(self) -> None:
        if '@adm' in current_user.username or '@op' in current_user.username: 
            messages = get_flashed_messages()
            produto_id = request.form.get('produto_id')
            produto_nome = request.form.get('produto_nome')
            produto_preco = request.form.get('produto_preco')
            produto_quantidade = request.form.get('produto_quantidade')
            
            form: FlaskForm = EditarProdutoForm()

            return render_template('dashboard/editar_estoque.html', form=form, produto_nome=produto_nome, produto_quantidade=produto_quantidade, produto_id=produto_id)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
    
    @login_required
    def alterar_estoque(self, produto_id):
        if '@adm' in current_user.username or '@op' in current_user.username:
            messages = get_flashed_messages() 
            form: FlaskForm = EditarProdutoForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    
                    input_dto = AlterEstoqueProdutoInputDto(**form.to_dict())

                    usecase: AlterEstoqueProdutoUseCase = current_app.global_usecases.alter_estoque_produto_usecase

                    estoque_entity = usecase.execute(input_dto=input_dto, produto_id=produto_id)

                    flash(message='Estoque Alterado', category='info')

                    return redirect(url_for('dashboard.estoque_produtos'))

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Alterar Quantidade', category='info')
                    pass

            return redirect(url_for('dashboard.estoque_produtos'))
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
    
    @login_required
    def add_produto(self):
        if '@adm' in current_user.username or '@op' in current_user.username: 
            messages = get_flashed_messages()
            form: FlaskForm = AddProdutoForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    
                    input_dto = CreateProdutoItemInputDto(**form.to_dict())

                    usecase: CreateProdutoUseCase = current_app.global_usecases.create_produto_usecase

                    usecase.execute(input_dto=input_dto)

                    file = form.file.data
                    if file:
                        original_filename = secure_filename(file.filename)
                        name, ext = os.path.splitext(original_filename)
                        name = input_dto.nome
                        new_filename = f"{name}{ext}"
                        file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], new_filename)
                        file.save(file_path)

                    flash(message='Produto Registrado', category='info')

                    return render_template('dashboard/add_produto.html', form=form)

                    pass
                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Registrar Produto', category='info')
                    pass

            return render_template('dashboard/add_produto.html', form=form)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
    
    @login_required
    def cultivo(self) -> None:
        if '@adm' in current_user.username or '@op' in current_user.username: 
            messages = get_flashed_messages()
            cultivo_id = request.form.get('cultivo_id')

            form: FlaskForm = AddColheitaForm()

            if form.validate_on_submit():
                try:
                    cultivo_id = int(cultivo_id)

                    pprint(form.to_dict())
                    
                    input_dto = CreateColheitaInputDto(**form.to_dict())

                    usecase: CreateColheitaUseCase = current_app.global_usecases.create_colheita_usecase

                    usecase.execute(input_dto=input_dto, cultivo_id=cultivo_id)

                    flash(message='Colheita Registrado', category='info')

                    return render_template('dashboard/add_cultivo.html', form=form, repositories=repositories)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Registrar Colheita', category='info')
                    pass
            
            cultivo_entity = repositories.cultivo_repository.get_cultivos_em_andamento()
            
            return render_template(
                'dashboard/cultivo.html',
                cultivos=cultivo_entity,
                form=form,
                repositories=repositories
                )
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401

    @login_required
    def add_cultivo(self):
        if '@adm' in current_user.username or '@op' in current_user.username: 
            messages = get_flashed_messages()
            form: FlaskForm = AddCultivoForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    
                    input_dto = CreateCultivoInputDto(**form.to_dict())

                    usecase: CreateCultivoUseCase = current_app.global_usecases.create_cultivo_usecase

                    usecase.execute(input_dto=input_dto)

                    flash(message='Cultivo Registrado', category='info')

                    return render_template('dashboard/add_cultivo.html', form=form, repositories=repositories)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Registrar Cultivo', category='info')
                    pass

            return render_template('dashboard/add_cultivo.html', form=form, repositories=repositories)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
        
    @login_required
    def buscar_alimentos(self) -> None:
        if '@adm' in current_user.username or '@op' in current_user.username: 
            messages = get_flashed_messages()
            form: FlaskForm = BuscarAlimentoForm()

            info_alimento = None

            msg_erro = ''

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    alimento = form.to_dict()

                    produto = alimento.get('alimento')
                    info_alimento = services.cohere_ia_service.obter_info_alimento(produto=produto)

                    if info_alimento != '"O parâmetro informado não é um alimento."':
                        info_alimento = json.loads(info_alimento)  
                    else:
                        info_alimento = {} 
                        msg_erro = 'O parâmetro informado não é um alimento.'

                    return render_template('dashboard/buscar_alimentos.html', form=form, info_alimento=info_alimento, msg_erro=msg_erro)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Buscar Alimento', category='info')
                    pass
            
            return render_template('dashboard/buscar_alimentos.html', form=form, info_alimento=info_alimento, msg_erro=msg_erro)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
        