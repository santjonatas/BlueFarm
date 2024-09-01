import traceback
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.forms.auth_forms.login_form import LoginForm

from app.application.settings.extensions import session

from app.application.use_cases.usuario.login_use_case import LoginUseCase, LoginInputDto
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity


login_blueprint = Blueprint('login', __name__, template_folder='views/templates')


@login_blueprint.route('/login', methods=['GET','POST'])
@login_blueprint.route('/login-funcionario', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            input_dto = LoginInputDto(**form.to_dict)

            use_case = LoginUseCase()

            output = use_case.execute(input=input_dto)

            

            # usuario_response = session.query(UsuarioEntity).filter(UsuarioEntity.username == form.username.data and UsuarioEntity.senha == form.senha.data).first()
            # session.commit()
            pass
            
        except Exception as e:
            flash(message=str(e), category='danger')
    
    return render_template('login.html', form=form)