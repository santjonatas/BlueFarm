from flask import current_app, flash, render_template, redirect, url_for, Blueprint
from flask_wtf import FlaskForm
from app.application.usecases.auth.create_administrador_usecase import CreateAdminUserUseCase
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.domain.forms.register_adm_form import RegisterAdmForm


class RegisterController:
    def __init__(self):
        self.blueprint = Blueprint('register', __name__, url_prefix='/auth')
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/register_admin/', view_func=self.register_admin, methods=['GET', 'POST'])
    
    def register_admin(self) -> None:
        form: FlaskForm = RegisterAdmForm()

        if form.validate_on_submit():
            try:
                input_dto = CreateAdminUserInputDto(**form.to_dict())

                usecase: CreateAdminUserUseCase = current_app.global_usecases.create_admin_user_usecase

                usecase.execute(input_dto=input_dto)

                flash(message='Administrador Registrado', category='info')

                return redirect(url_for('login.login'))
            except Exception as e:
                flash(message=str(e), category='danger')
        
        return render_template('auth/registro_admin.html', form=form)
