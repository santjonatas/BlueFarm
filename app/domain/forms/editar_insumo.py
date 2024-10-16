from flask import current_app
from app.domain.forms.common.base_form import BaseForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class EditarInsumoForm(BaseForm):
    quantidade_disponivel = IntegerField('Quantidade disponível',
        validators=[DataRequired()
    ])

    submit = SubmitField('Upload')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> dict:
        return {
            'quantidade_disponivel': self.quantidade_disponivel.data
        }
