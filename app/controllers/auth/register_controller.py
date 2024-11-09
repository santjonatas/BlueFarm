from pprint import pprint
from flask import current_app, flash, get_flashed_messages, jsonify, render_template, redirect, url_for, Blueprint
from flask_login import login_required, login_user, logout_user, current_user
from flask_wtf import FlaskForm
from app.application.usecases.auth.create_administrador_usecase import CreateAdminUserUseCase
from app.application.usecases.auth.create_operador_usecase import CreateOperadorUserUseCase
from app.application.usecases.dto.input.users.create_admin_user_input_dto import CreateAdminUserInputDto
from app.application.usecases.dto.input.users.create_operador_user_input_dto import CreateOperadorUserInputDto
from app.domain.forms.register_adm_form import RegisterAdmForm
from app.domain.forms.register_op_form import RegisterOpForm


class RegisterController:
    def __init__(self):
        self.blueprint = Blueprint('register', __name__, url_prefix='/auth')
        self.register_routes()

    def register_routes(self):
        self.blueprint.add_url_rule('/register_admin/', view_func=self.register_admin, methods=['GET', 'POST'])
        self.blueprint.add_url_rule('/register_operador/', view_func=self.register_operador, methods=['GET', 'POST'])
    
    @login_required
    def register_admin(self) -> None:
        if '@adm' in current_user.username: 
            messages = get_flashed_messages()
            form: FlaskForm = RegisterAdmForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    input_dto = CreateAdminUserInputDto(**form.to_dict())

                    usecase: CreateAdminUserUseCase = current_app.global_usecases.create_admin_user_usecase

                    usecase.execute(input_dto=input_dto)

                    flash(message='Administrador Registrado', category='info')

                    return redirect(url_for('register.register_admin'))
                except Exception as e:
                    flash(message=str(e), category='danger')
                    return redirect(url_for('register.register_admin'))
                
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f"{field}: {error}", category='danger')
                return redirect(url_for('register.register_admin'))
            
            return render_template('auth/registro_admin.html', form=form)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401
    
    @login_required
    def register_operador(self) -> None:
        if '@adm' in current_user.username: 
            messages = get_flashed_messages()
            form: FlaskForm = RegisterOpForm()

            if form.validate_on_submit():
                try:
                    pprint(form.to_dict())
                    input_dto = CreateOperadorUserInputDto(**form.to_dict())

                    usecase: CreateOperadorUserUseCase = current_app.global_usecases.create_operador_user_usecase

                    usecase.execute(input_dto=input_dto)

                    flash(message='Operador Registrado', category='info')

                    return redirect(url_for('register.register_operador'))
                except Exception as e:
                    flash(message=str(e), category='danger')
                    return redirect(url_for('register.register_operador'))
                
            if form.errors:
                for field, errors in form.errors.items():
                    for error in errors:
                        flash(f"{field}: {error}", category='danger')
                return redirect(url_for('register.register_operador'))
            
            return render_template('auth/registro_operador.html', form=form)
        else:
            return jsonify({"message": "Acesso não autorizado"}), 401