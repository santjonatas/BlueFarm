from datetime import datetime
import os
import traceback
from flask import current_app, flash, render_template, redirect, url_for, jsonify, request, session, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from decimal import Decimal
import qrcode
import uuid
from PIL import Image
import requests

from app.application.config.global_repositories import GlobalRepositories
from app.application.usecases.dto.input.entities.create_pagamento_item_input_dto import CreatePagamentoInputDto
from app.application.usecases.dto.input.entities.create_pedido_input_dto import CreatePedidoInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.pedido.create_pagamento_usecase import CreatePagamentoUseCase
from app.application.usecases.pedido.create_pedido_usecase import CreatePedidoUseCase

import os
from dotenv import load_dotenv

load_dotenv()

repositories = GlobalRepositories()

class MainController:
    def __init__(self):
        self.blueprint = Blueprint('main', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/main/', view_func=self.main, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/main_client/', view_func=self.main_client, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/add_to_cart/', view_func=self.add_to_cart, methods=['POST'])
        self.blueprint.add_url_rule('/remove_from_cart/', view_func=self.remove_from_cart, methods=['POST'])
        self.blueprint.add_url_rule('/increment_item/', view_func=self.increment_item, methods=['POST'])
        self.blueprint.add_url_rule('/decrement_item/', view_func=self.decrement_item, methods=['POST'])
        self.blueprint.add_url_rule('/fazer_pedido/', view_func=self.fazer_pedido, methods=['POST'])
        self.blueprint.add_url_rule('/fazer_pagamento/', view_func=self.fazer_pagamento, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/confirm/<qr_id>', view_func=self.acessar_qr_code, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/confirmar_pagamento/<qr_id>', view_func=self.confirmar_pagamento, methods=['GET', 'POST'])

    @login_required
    def main(self) -> None:
        return render_template('main/main.html')

    def logout(self) -> None:
        logout_user()
        return redirect(url_for('login.login'))
    
    @login_required
    def main_client(self) -> None:
        if 'carrinho' not in session:
            session['carrinho'] = []
        
        produto_entity = repositories.produto_repository.list()
        
        pedidos_entity = repositories.pedido_repository.get_pedidos_by_cliente(id_cliente=current_user.cliente.id)

        total_precos = sum(Decimal(item['preco']) for item in session['carrinho'] if 'preco' in item)
        
        return render_template(
            'main/main_client.html',
            produtos=produto_entity, 
            total_precos=total_precos, 
            pedidos=pedidos_entity,
            repositories=repositories
            )

    @login_required
    def remove_from_cart(self):
        produto_id = int(request.form.get('produto_id'))

        if 'carrinho' in session:
            session['carrinho'] = [item for item in session['carrinho'] if item['id'] != produto_id]

        print(f'removeu: {session['carrinho']}') 
        flash('Produto removido do carrinho!')
        return redirect(url_for('main.main_client'))

    @login_required
    def add_to_cart(self):
        produto_id = request.form.get('produto_id')
        produto_entity = repositories.produto_repository.get(obj_id=produto_id)

        if 'carrinho' not in session:
            session['carrinho'] = []

        if produto_entity:
            preco_produto = Decimal(produto_entity.preco) if produto_entity.preco is not None else Decimal('0.00')
            
            for item in session['carrinho']:
                if item['id'] == produto_entity.id:
                    item['quantidade'] += 1
                    item['preco'] = Decimal(item['preco'])  
                    item['preco'] += Decimal(produto_entity.preco)  
                    break
            else:
                session['carrinho'].append({
                    'id': produto_entity.id,
                    'nome': produto_entity.nome,
                    'preco': preco_produto,
                    'quantidade': 1
                })
        print(session['carrinho'])  
        flash('Produto adicionado ao carrinho!')
        return redirect(url_for('main.main_client'))

    @login_required
    def increment_item(self):
        produto_id = int(request.form.get('produto_id'))
        produto_entity = repositories.produto_repository.get(obj_id=produto_id)

        if 'carrinho' in session:
            for item in session['carrinho']:
                if item['id'] == produto_id:
                    item['quantidade'] += 1
                    item['preco'] = Decimal(item['preco']) 
                    item['preco'] += Decimal(produto_entity.preco)   
                    break

        flash('Quantidade incrementada!')
        return redirect(url_for('main.main_client'))
    
    @login_required
    def decrement_item(self):
        produto_id = int(request.form.get('produto_id'))
        produto_entity = repositories.produto_repository.get(obj_id=produto_id)

        if 'carrinho' in session:
            for item in session['carrinho']:
                if item['id'] == produto_id:
                    item['quantidade'] -= 1
                    item['preco'] = Decimal(item['preco']) 
                    item['preco'] -= Decimal(produto_entity.preco) 

                    if item['quantidade'] == 0:
                        session['carrinho'].remove(item) 
                    break

        flash('Quantidade decrementada!')
        return redirect(url_for('main.main_client'))
    

    @login_required
    def fazer_pedido(self):
        try:
            input_dto = CreatePedidoInputDto(
                id_cliente = current_user.cliente.id,
                data_pedido = datetime.now(),
                status ='Aguardando Pagamento',
                valor_total = sum(Decimal(item['preco']) for item in session['carrinho'] if 'preco' in item)
            )

            usecase: CreatePedidoUseCase = current_app.global_usecases.create_pedido_usecase

            pedido_entity = usecase.execute(input_dto=input_dto, list_carrinho=session['carrinho'])

            flash(message='Operador Registrado', category='info')

            session['carrinho'] = []

            return redirect(url_for('main.main_client'))
        except Exception as e:
            stacktrace = traceback.format_exc()
            flash(message=str(e), category='danger')

        return redirect(url_for('main.main_client'))
    
    @login_required
    def fazer_pagamento(self):
        pedido_id = request.form.get('pedido_id') 
        print(pedido_id)
        id_qr_code = pedido_id

        def obter_url_ngrok():
            try:
                ngrok = os.getenv('HTTP_NGROK')
                response = requests.get(ngrok)
                tunnels = response.json().get('tunnels', [])
                if tunnels:
                    return tunnels[0]['public_url'] 
            except Exception as e:
                print(f"Erro ao obter URL do ngrok: {e}")
            return None

        def gerar_qr_code():
            ngrok_url = obter_url_ngrok()

            if ngrok_url is not None:   
                qr_id = str(pedido_id)
                qr_data = f"{ngrok_url}/confirm/{qr_id}"
                
                qr_img = qrcode.make(qr_data)
                qr_img.save(f"app/views/static/qr_codes/{qr_id}.png")
            
                return qr_id

        if not os.path.exists(f"app/views/static/qr_codes/{pedido_id}.png"):
            id_qr_code = gerar_qr_code()

        return render_template('main/pagamento.html', qr_id=id_qr_code)

    def acessar_qr_code(self, qr_id):
        if request.method == 'POST':
            if session.get(f'{qr_id}_confirmed'):
                return "QR Code já foi confirmado!"
            
            session[f'{qr_id}_confirmed'] = True
            return "Pagamento confirmado com sucesso!"
        
        return render_template('main/acessar_qr_code.html', qr_id=qr_id)

    def confirmar_pagamento(self, qr_id):
        print(qr_id)
        try:
            input_dto = CreatePagamentoInputDto(
                id_pedido=qr_id,
                metodo_pagamento='QR Code',
                data_pagamento=datetime.now(),
                status_pagamento='Pago'
            )

            usecase: CreatePagamentoUseCase = current_app.global_usecases.create_pagamento_usecase

            pagamento_entity = usecase.execute(input_dto=input_dto)

            flash(message='Pagamento Realizado', category='info')

            return render_template('main/confirmar_pagamento.html', qr_id=qr_id)
        
        except Exception as e:
            stacktrace = traceback.format_exc()
            flash(message=str(e), category='danger')
        
        return render_template('main/confirmar_pagamento.html', qr_id=qr_id)
