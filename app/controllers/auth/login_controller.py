from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_login import login_user, logout_user
from flask_wtf import FlaskForm
from app.application.usecases.auth.validate_user_usecase import ValidateUserUseCase
from app.application.usecases.dto.input.auth.validate_user_input_dto import ValidateUserInputDto
from app.domain.forms.login_form import LoginForm


class LoginController:
    def __init__(self):
        self.blueprint = Blueprint('login', __name__, url_prefix='/auth')
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/login/', view_func=self.login, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/logout/', view_func=self.logout)
    
    def login(self) -> None:
        form: FlaskForm = LoginForm()

        if form.validate_on_submit():
            try:
                input_dto = ValidateUserInputDto(**form.to_dict)
                usecase = ValidateUserUseCase(
                    global_utils=current_app.global_utils,
                    usuario_service=current_app.global_services.usuario_service)
                
                output_dto = usecase.execute(input_dto=input_dto)

                login_user(output_dto.usuario)

                #
                if '@adm' in output_dto.usuario.username:
                    return redirect(url_for('main.main'))
                
                if not '@adm' in output_dto.usuario.username and not '@op' in output_dto.usuario.username:
                    return redirect(url_for('main.main_client'))
                #

                # return redirect(url_for('main.main'))

            except Exception as e:
                flash(message=str(e), category='danger')
        
        return render_template('auth/login.html', form=form)

    def logout(self) -> None:
        logout_user()
        return redirect(url_for('login.login'))
