import traceback
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.models.entities.usuario_management.usuario_entity import UsuarioEntity

from app.application.settings.extensions import session



home_controller = Blueprint('home', __name__, template_folder='views/templates')


@home_controller.route('/home', methods=['GET','POST'])
@login_required
def home():

    print(f"Usuário autenticado: {current_user.is_authenticated}")
    print(f"ID do usuário: {current_user.id if current_user.is_authenticated else 'Usuário não autenticado'}")
    
    try:

        return render_template('home.html')

    except Exception as e:
        stacktrace = traceback.format_exc()
        flash(message=str(e), category='danger')
            
