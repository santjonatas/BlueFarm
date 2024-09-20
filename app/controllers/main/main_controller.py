from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_login import login_user, logout_user


class MainController:
    def __init__(self):
        self.blueprint = Blueprint('main', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/main/', view_func=self.main, methods=['GET', 'POST'])
    
    def main(self) -> None:
        
        return render_template('main.html')

    def logout(self) -> None:
        logout_user()
        return redirect(url_for('login.login'))
