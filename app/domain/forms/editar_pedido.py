from flask import current_app
from app.domain.forms.common.base_form import BaseForm
from wtforms import IntegerField, SubmitField, StringField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length
from flask_wtf.file import FileAllowed

class EditarPedidoForm(BaseForm):
    status = StringField('Nome',
        validators=[DataRequired(),
            Length(min=2, message="O status deve ter pelo menos 2 caracteres.")
    ])

    submit = SubmitField('Upload')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> dict:
        return {
            'status': self.status.data
        }
