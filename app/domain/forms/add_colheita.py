from flask import current_app
from app.application.config.global_repositories import GlobalRepositories
from app.domain.entities.cultivo_entity import CultivoEntity
from app.domain.entities.insumo_entity import InsumoEntity
from app.domain.forms.common.base_form import BaseForm
from wtforms import SelectField, StringField, PasswordField, DateField, DecimalField, EmailField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email
from flask_wtf.file import FileAllowed


repositories = GlobalRepositories()

class AddColheitaForm(BaseForm):
    quantidade = IntegerField('Quantidade de Produtos Colhidos',
        validators=[DataRequired()
    ])
    data = DateField('Data de Colheita',
        validators=[Optional()] 
    )
    submit = SubmitField('Upload')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def to_dict(self) -> dict:
        return {
            'quantidade': self.quantidade.data,
            'data': self.data.data
        }
