import traceback
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.forms.auth_forms.registro_operador_form import RegistroOperadorForm 

from app.application.settings.extensions import session

from app.application.use_cases.usuario.registrar_operador_use_case import RegistrarOperadorUseCase
from app.application.use_cases.usuario.registrar_operador_use_case import RegistrarOperadorInputDto


registro_operador_blueprint = Blueprint('registro-operador', __name__, template_folder='views/templates')


@registro_operador_blueprint.route('/registro-operador', methods=['GET','POST'])
def login():
    form = RegistroOperadorForm()
    if form.validate_on_submit():
        try:
            input_dto = RegistrarOperadorInputDto(**form.to_dict)

            use_case = RegistrarOperadorUseCase()

            use_case.execute(input=input_dto)
            pass
            
        except Exception as e:
            stacktrace = traceback.format_exc()
            flash(message=str(e), category='danger')
     
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash(message=f"Erro no campo {field}: {error}", category='danger')
    
    return render_template('registro_operador.html', form=form)