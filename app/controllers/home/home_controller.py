import traceback
from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user


class HomeController:
    def __init__(self):
        self.blueprint = Blueprint('home', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/home', view_func=self.home, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/', view_func=self.index)

    def home(self) -> None:
        try:
            return render_template('home/home.html')
        except Exception as e:
            stacktrace = traceback.format_exc()
            return e
        
    def index(self) -> None:
        return redirect(url_for('home.home'))

    def login(self) -> None:
        try:
            return redirect(url_for('login.login'))
        except Exception as e:
            return e