from flask import current_app, flash, render_template, redirect, url_for, jsonify, request, session, Blueprint
from flask_login import login_required, login_user, logout_user
from decimal import Decimal


from app.application.config.global_repositories import GlobalRepositories

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
        ####################
        self.blueprint.add_url_rule('/decrement_item/', view_func=self.decrement_item, methods=['POST'])


    @login_required
    def main(self) -> None:
        return render_template('main/main.html')

    def logout(self) -> None:
        logout_user()
        return redirect(url_for('login.login'))
    
    @login_required
    def main_client(self) -> None:
        produto_entity = repositories.produto_repository.list()
        return render_template('main/main_client.html', produtos=produto_entity)


    @login_required
    def remove_from_cart(self):
        produto_id = int(request.form.get('produto_id'))

        if 'carrinho' in session:
            session['carrinho'] = [item for item in session['carrinho'] if item['id'] != produto_id]

        print(f'removeu: {session['carrinho']}') 
        flash('Produto removido do carrinho!')
        return redirect(url_for('main.main_client'))
    
#####################################

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
    
    #####################################

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
    

    ########################################
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
                    break

        flash('Quantidade decrementada!')
        return redirect(url_for('main.main_client'))