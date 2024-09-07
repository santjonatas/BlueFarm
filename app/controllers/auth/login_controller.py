from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm


class LoginController:
    def __init__(self):
        self.blueprint = Blueprint('login', __name__, url_prefix='/auth')
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/login/', view_func=self.login, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/logout/', view_func=self.logout)
    
    def login(self) -> None:
        pass

    def logout(self) -> None:
        logout_user()
        return redirect(url_for('login.login'))
