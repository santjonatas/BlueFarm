import traceback
from pprint import pprint
from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_login import login_required, current_user
from flask_wtf import FlaskForm

from app.application.usecases.auth.create_cliente_usecase import CreateClienteUserUseCase
from app.application.usecases.dto.input.users.create_cliente_user_input_dto import CreateClienteUserInputDto
from app.domain.forms.register_client_form import RegisterClientForm


class HomeController:
    def __init__(self):
        self.blueprint = Blueprint('home', __name__)
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/home', view_func=self.home, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/', view_func=self.index)
        
        
    def index(self) -> None:
        return redirect(url_for('home.home'))
    

    def home(self) -> None:
        form: FlaskForm = RegisterClientForm()

        if form.validate_on_submit():
            try:
                pprint(form.to_dict())
                input_dto = CreateClienteUserInputDto(**form.to_dict())

                usecase: CreateClienteUserUseCase = current_app.global_usecases.create_cliente_user_usecase

                usecase.execute(input_dto=input_dto)

                flash(message='Cliente Registrado', category='info')

                return render_template('home/home.html')
            except Exception as e:
                flash(message=str(e), category='danger')
        
        return render_template('home/home.html', form=form)
