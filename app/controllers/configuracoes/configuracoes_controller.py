from datetime import datetime
import os
from pprint import pprint
import re
import traceback
from flask import current_app, flash, render_template, redirect, url_for, jsonify, request, session, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from decimal import Decimal
from werkzeug.utils import secure_filename
import json

from app.application.config.global_repositories import GlobalRepositories
from app.application.config.global_services import GlobalServices
from app.application.usecases.auth.alter_estoque_produto_usecase import AlterEstoqueProdutoUseCase
from app.application.usecases.auth.create_cargo_usecase import CreateCargoUseCase
from app.application.usecases.auth.create_colheita_usecase import CreateColheitaUseCase
from app.application.usecases.auth.create_cultivo_usecase import CreateCultivoUseCase
from app.application.usecases.auth.create_departamento_usecase import CreateDepartamentoUseCase
from app.application.usecases.auth.create_produto_usecase import CreateProdutoUseCase
from app.application.usecases.auth.remove_funcionario_usecase import RemoveFuncionarioUseCase
from app.application.usecases.dto.input.entities.create_cargo_input_dto import CreateCargoInputDto
from app.application.usecases.dto.input.entities.create_departamento_input_dto import CreateDepartamentoInputDto
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
from app.domain.forms.add_cargo import AddCargoForm
from app.domain.forms.add_colheita import AddColheitaForm
from app.domain.forms.add_cultivo import AddCultivoForm
from app.domain.forms.add_departamento import AddDepartamentoForm
from app.domain.forms.add_produto import AddProdutoForm
from flask_wtf import FlaskForm

from app.domain.forms.buscar_alimento import BuscarAlimentoForm
from app.domain.forms.editar_produto import EditarProdutoForm
from app.domain.forms.remover_funcionario import RemoverFuncionarioForm

repositories = GlobalRepositories()
services = GlobalServices(global_repositories=repositories)

class ConfiguracoesController:
    def __init__(self):
        self.blueprint = Blueprint('configuracoes', __name__)
        self.register_routes()

    def register_routes(self): 
        self.blueprint.add_url_rule('/departamentos/', view_func=self.departamentos, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/cargos/', view_func=self.cargos, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/remover_funcionario/<id_funcionario>', view_func=self.remover_funcionario, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/funcionarios/', view_func=self.funcionarios, methods=['GET', 'POST'])
    
    @login_required
    def departamentos(self) -> None:
        if '@adm' in current_user.username: 
            departamento_entity = repositories.departamento_repository.list()

            form: FlaskForm = AddDepartamentoForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    
                    input_dto = CreateDepartamentoInputDto(**form.to_dict())

                    usecase: CreateDepartamentoUseCase = current_app.global_usecases.create_departamento_usecase

                    usecase.execute(input_dto=input_dto)

                    flash(message='Departamento Registrado', category='info')

                    return render_template('configuracoes/departamentos.html', form=form, departamentos=departamento_entity)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Registrar Departamento', category='info')
                    pass
            
            return render_template(
                'configuracoes/departamentos.html',
                form=form,
                departamentos=departamento_entity
                )
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401

    @login_required
    def cargos(self) -> None:
        if '@adm' in current_user.username: 
            cargo_entity = repositories.cargo_repository.list()

            form: FlaskForm = AddCargoForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    
                    input_dto = CreateCargoInputDto(**form.to_dict())

                    usecase: CreateCargoUseCase = current_app.global_usecases.create_cargo_usecase

                    usecase.execute(input_dto=input_dto)

                    flash(message='Cargo Registrado', category='info')

                    return render_template('configuracoes/cargos.html', form=form, cargos=cargo_entity)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Registrar Cargo', category='info')
                    pass
            
            return render_template(
                'configuracoes/cargos.html',
                form=form,
                cargos=cargo_entity
                )
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401

    @login_required
    def funcionarios(self) -> None:
        if '@adm' in current_user.username: 
            form = RemoverFuncionarioForm()

            funcionario_entity = repositories.funcionario_repository.list()
            
            return render_template('configuracoes/funcionarios.html', form=form, funcionarios=funcionario_entity)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401

    @login_required
    def remover_funcionario(self, id_funcionario) -> None:
        if '@adm' in current_user.username: 
            funcionario_entity = repositories.funcionario_repository.list()

            form: FlaskForm = RemoverFuncionarioForm()

            if form.validate_on_submit():
                try:
                    usecase: RemoveFuncionarioUseCase = current_app.global_usecases.remove_funcionario_usecase

                    usecase.execute(id_funcionario=id_funcionario)

                    flash(message='Funcionário Deletado', category='info')

                    return render_template('configuracoes/funcionarios.html', form=form, funcionarios=funcionario_entity)

                except Exception as e:
                    stacktrace = traceback.format_exc()
                    flash(message='Erro ao Deletar Funcionário', category='info')
                    pass
            
            return render_template(
                'configuracoes/funcionarios.html',
                form=form,
                funcionarios=funcionario_entity
                )
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
