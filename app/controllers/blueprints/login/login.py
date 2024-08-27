from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.forms.auth_forms.login_form import LoginForm

#
from app.application.settings.extensions import session
#
from app.models.entities.usuario_entity import UsuarioEntity


login_blueprint = Blueprint('login', __name__, template_folder='views/templates')


@login_blueprint.route('/login', methods=['GET','POST'])
@login_blueprint.route('/login-funcionario', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        try:
            #
            print(form.username.data)
            print(form.senha.data)
            #
            usuario = UsuarioEntity(username=form.username.data, senha=form.senha.data)
            session.add(usuario)
            session.commit()
            
        except Exception as e:
            flash(message=str(e), category='danger')
    
    return render_template('login.html', form=form)