import os
from dotenv import load_dotenv
from app.domain.forms.common.base_form import BaseForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Length, Regexp

load_dotenv()


class LoginForm(BaseForm):
    username = StringField('Username',
        validators=[DataRequired(),
            Length(min=4,
                max=50,
                message="O username deve ter entre 4 e 20 caracteres."),
                Regexp(r'^[\w@]+$', message="O username deve conter apenas letras, números e underscores.")])

    senha = PasswordField('Senha',
        validators=[DataRequired(),
        Length(min=8, message="A senha deve ter no mínimo 8 caracteres."),
        Regexp(os.getenv('PASSWORD_REGEX'),
            message="A senha deve ter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")])

    @property
    def to_dict(self) -> dict:
        return {
            "username": self.username.data,
            "senha": self.senha.data
        }
