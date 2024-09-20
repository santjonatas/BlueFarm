import traceback
from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user


class HomeController:
    def __init__(self):
        self.blueprint = Blueprint('home', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/home', view_func=self.home, methods=['GET', 'POST'])

    @login_required
    def home(self) -> None:
        try:
            return render_template('home.home')
        except:
            return 'erro'