from flask import Blueprint
from flask_login import login_required, current_user


class HomeController:
    def __init__(self):
        self.blueprint = Blueprint('home', __name__, url_prefix='/home')
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/', view_func=self.index, methods=['GET', 'POST'])

    @login_required
    def index(self):
        try:
            return current_user.pessoa.nome
        except:
            return current_user.username
