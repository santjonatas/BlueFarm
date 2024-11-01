from flask import current_app
from app.application.config.global_repositories import GlobalRepositories
from app.domain.entities.cultivo_entity import CultivoEntity
from app.domain.entities.insumo_entity import InsumoEntity
from app.domain.forms.common.base_form import BaseForm
from wtforms import SelectField, StringField, PasswordField, DateField, DecimalField, EmailField, IntegerField, FileField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email
from flask_wtf.file import FileAllowed


repositories = GlobalRepositories()

class AddCargoForm(BaseForm):
    id_nivel = BooleanField('Id Nível')
    funcao = StringField('Função',
        validators=[DataRequired(),
            Length(min=2, message="A função deve ter pelo menos 2 caracteres.")
    ])
    salario = DecimalField('Salário',
        validators=[DataRequired()
    ])
    submit = SubmitField('Upload')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def to_dict(self) -> dict:
        return {
            'id_nivel': self.id_nivel.data,
            'funcao': self.funcao.data,
            'salario': self.salario.data
        }
