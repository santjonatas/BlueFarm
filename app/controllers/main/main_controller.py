from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_login import login_required, login_user, logout_user

from app.application.config.global_repositories import GlobalRepositories

repositories = GlobalRepositories()

class MainController:
    def __init__(self):
        self.blueprint = Blueprint('main', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/main/', view_func=self.main, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/main_client/', view_func=self.main_client, methods=['GET', 'POST'])
    
    @login_required
    def main(self) -> None:
        
        return render_template('main/main.html')

    def logout(self) -> None:
        logout_user()
        return redirect(url_for('login.login'))
    
    @login_required
    def main_client(self) -> None:

        produto_entity = repositories.produto_repository.list()
        print(produto_entity)

        return render_template('main/main_client.html', produtos=produto_entity)
