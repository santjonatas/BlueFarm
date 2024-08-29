from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.forms.auth_forms.registro_form import RegistroForm # importar registro form
#
from app.application.settings.extensions import session
#
from app.models.entities.usuario_management.pessoa_entity import PessoaEntity
from app.models.entities.usuario_management.funcionario_entity import FuncionarioEntity
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity
from app.models.entities.usuario_management.administrador_entity import AdministradorEntity
from app.models.entities.usuario_management.operador_entity import OperadorEntity


registro_blueprint = Blueprint('registro', __name__, template_folder='views/templates')


@registro_blueprint.route('/registro', methods=['GET','POST'])
@registro_blueprint.route('/registro-funcionario', methods=['GET','POST'])
def login():
    form = RegistroForm()
    if form.validate_on_submit():
        try:
            #
            print(form.username.data)
            print(form.senha.data)
            #

            # usuario_response = session.query(UsuarioEntity).filter(UsuarioEntity.username == form.username.data and UsuarioEntity.senha == form.senha.data).first()
            # session.commit()
            
        except Exception as e:
            flash(message=str(e), category='danger')
    
    return render_template('registro.html', form=form)