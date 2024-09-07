from flask_wtf import FlaskForm
from wtforms import SubmitField


class BaseForm(FlaskForm):
    submit = SubmitField('entrar')
