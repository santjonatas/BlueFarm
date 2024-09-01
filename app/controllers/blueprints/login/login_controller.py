import traceback
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.models.forms.auth_forms.login_form import LoginForm

from app.application.settings.extensions import session

from app.application.use_cases.usuario.login_use_case import LoginUseCase, LoginInputDto
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity


login_controller_blueprint = Blueprint('login', __name__, template_folder='views/templates')


@login_controller_blueprint.route('/login', methods=['GET','POST'])
@login_controller_blueprint.route('/login-funcionario', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            input_dto = LoginInputDto(**form.to_dict)

            use_case = LoginUseCase()

            output = use_case.execute(input=input_dto)

            login_user(output.usuario)
            
            return f'Usuário logado'

        except Exception as e:
            stacktrace = traceback.format_exc()
            flash(message=str(e), category='danger')
            
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(message=f"Erro no campo {field}: {error}", category='danger')
    
    return render_template('login.html', form=form)