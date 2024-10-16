from flask import current_app
from app.application.config.global_repositories import GlobalRepositories
from app.domain.entities.cultivo_entity import CultivoEntity
from app.domain.entities.insumo_entity import InsumoEntity
from app.domain.forms.common.base_form import BaseForm
from wtforms import SelectField, StringField, PasswordField, DateField, DecimalField, EmailField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email
from flask_wtf.file import FileAllowed


repositories = GlobalRepositories()

class BuscarAlimentoForm(BaseForm):
    alimento = StringField('Alimento',
        validators=[DataRequired()
    ])
    submit = SubmitField('Upload')           


    def to_dict(self) -> dict:
        return {
            'alimento': self.alimento.data
        }
