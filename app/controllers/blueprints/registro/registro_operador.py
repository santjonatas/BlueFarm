from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models.forms.auth_forms.registro_operador_form import RegistroOperadorForm 
#
from app.application.settings.extensions import session
#
from app.application.use_cases.usuario.registrar_operador_use_case import RegistrarOperadorUseCase

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
            registrar_operador_use_case = RegistrarOperadorUseCase(
                nome= form.nome.data, 
                data_nascimento= form.data_nascimento.data, 
                cpf= form.cpf.data, 
                genero= form.genero.data, 
                telefone= form.telefone.data, 
                email= form.email.data, 
                endereco= form.endereco.data, 
                data_admissao= form.data_admissao.data, 
                cargo= form.cargo.data, 
                salario= form.salario.data,
                data_demissao= form.data_demissao.data, 
                username= form.username.data, 
                senha= form.senha.data,
                permissao= form.permissao.data, 
                area_operacao= form.area_operacao.data, 
                supervisor_direto= form.supervisor_direto.data
            )

            registrar_operador_use_case.execute()
            pass
            
        except Exception as e:
            flash(message=str(e), category='danger')
    
    return render_template('registro_operador.html', form=form)