from flask import Blueprint, render_template, request, redirect, url_for


login_blueprint = Blueprint('login', __name__, template_folder='views/templates')


@login_blueprint.route('/login', methods=['GET','POST'])
@login_blueprint.route('/login-funcionario', methods=['GET','POST'])
def login():
    
    return render_template('login.html')