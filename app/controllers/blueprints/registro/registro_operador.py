from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.forms.auth_forms.registro_operador_form import RegistroOperadorForm 
#
from app.application.settings.extensions import session
#
from app.models.entities.usuario_management.pessoa_entity import PessoaEntity
from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity
from app.models.entities.usuario_management.administrador_entity import AdministradorEntity
from app.models.entities.usuario_management.operador_entity import OperadorEntity


registro_operador_blueprint = Blueprint('registro-operador', __name__, template_folder='views/templates')


@registro_operador_blueprint.route('/registro-operador', methods=['GET','POST'])
def login():
    form = RegistroOperadorForm()
    if form.validate_on_submit():
        try:
            

            # usuario_response = session.query(UsuarioEntity).filter(UsuarioEntity.username == form.username.data and UsuarioEntity.senha == form.senha.data).first()
            # session.commit()
            pass
            
        except Exception as e:
            flash(message=str(e), category='danger')
    
    return render_template('registro_operador.html', form=form)