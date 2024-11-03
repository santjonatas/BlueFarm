from pprint import pprint
import traceback
from flask import current_app, flash, get_flashed_messages, render_template, redirect, session, url_for, Blueprint
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm
from app.application.usecases.auth.create_operador_usecase import CreateOperadorUserUseCase
from app.application.usecases.auth.update_perfil_usecase import UpdatePerfilUserUseCase
from app.application.usecases.auth.validate_user_usecase import ValidateUserUseCase
from app.application.usecases.dto.input.auth.validate_user_input_dto import ValidateUserInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.application.usecases.dto.input.users.update_perfil_user_input_dto import UpdatePerfilUserInputDto
from app.domain.forms.atualizar_perfil_form import AtualizarPerfilForm
from app.domain.forms.login_form import LoginForm
from app.domain.forms.register_op_form import RegisterOpForm

from flask_login import login_required, login_user, logout_user, current_user


class LoginController:
    def __init__(self):
        self.blueprint = Blueprint('login', __name__, url_prefix='/auth')
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/login/', view_func=self.login, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/logout/', view_func=self.logout)
        self.blueprint.add_url_rule('/perfil/', view_func=self.perfil, methods=['GET', 'POST'])
    
    def login(self) -> None:
        messages = get_flashed_messages()
        
        form: FlaskForm = LoginForm()

        if form.validate_on_submit():
            try:
                input_dto = ValidateUserInputDto(**form.to_dict)
                usecase = ValidateUserUseCase(
                    global_utils=current_app.global_utils,
                    usuario_service=current_app.global_services.usuario_service)
                
                output_dto = usecase.execute(input_dto=input_dto)

                login_user(output_dto.usuario)

                if '@adm' in output_dto.usuario.username:
                    return redirect(url_for('main.main'))
                
                if '@op' in output_dto.usuario.username:
                    return redirect(url_for('main.main'))
                
                if not '@adm' in output_dto.usuario.username and not '@op' in output_dto.usuario.username:
                    return redirect(url_for('main.main_client'))

            except Exception as e:
                stacktracr = traceback.format_exc()
                flash(message=str(e), category='danger')
        
        return render_template('auth/login.html', form=form)

    def logout(self) -> None:
        logout_user()
        return redirect(url_for('login.login'))


    def perfil(self) -> None:
        messages = get_flashed_messages()
        form: FlaskForm = AtualizarPerfilForm()

        if form.validate_on_submit():
            try:
                pprint(form.to_dict())
                input_dto = UpdatePerfilUserInputDto(**form.to_dict())

                usecase: UpdatePerfilUserUseCase = current_app.global_usecases.update_perfil_user_usecase

                usecase.execute(input_dto=input_dto, id_pessoa=current_user.id)

                flash(message='Perfil Atualizado', category='info')

                return render_template('auth/perfil.html', form=form)
            except Exception as e:
                flash(message=str(e), category='danger')

        return render_template('auth/perfil.html', form=form)
