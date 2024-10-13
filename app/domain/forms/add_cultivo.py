from flask import current_app
from app.application.config.global_repositories import GlobalRepositories
from app.domain.entities.cultivo_entity import CultivoEntity
from app.domain.entities.insumo_entity import InsumoEntity
from app.domain.forms.common.base_form import BaseForm
from wtforms import SelectField, StringField, PasswordField, DateField, DecimalField, EmailField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email
from flask_wtf.file import FileAllowed


repositories = GlobalRepositories()

class AddCultivoForm(BaseForm):
    id_insumo = SelectField('Insumo',
        coerce=int,
        validators=[DataRequired()
    ])
    quantidade = IntegerField('Quantidade de Insumos',
        validators=[DataRequired()
    ])
    status = StringField('Status',
        validators=[DataRequired(),
            Length(min=2, message="O status do cultivo deve ter pelo menos 2 caracteres.")
    ])
    data_inicio = DateField('Data de Início',
        validators=[DataRequired()]
    )
    data_fim = DateField('Data de Colheita',
        validators=[DataRequired()]
    )
    
    submit = SubmitField('Upload')

    def __init__(self, *args, **kwargs):

        with current_app.app_context():

            self.id_insumo.choices = [(insumo.id) for insumo in InsumoEntity.query.all()]
           

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> dict:
        return {
            'id_insumo': self.id_insumo.data,
            'quantidade': self.quantidade.data,
            'status': self.status.data,
            'data_inicio': self.data_inicio.data,
            'data_fim': self.data_fim.data
        }
