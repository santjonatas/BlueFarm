from flask import current_app
from app.domain.entities.administrador_entity import AdministradorEntity
from app.domain.entities.cargo_entity import CargoEntity
from app.domain.entities.departamento_entity import DepartamentoEntity
from app.domain.forms.common.base_form import BaseForm
from wtforms import SelectField, StringField, PasswordField, DateField, DecimalField, EmailField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email

class AtualizarPerfilForm(BaseForm):
    genero = SelectField('Gênero', validators=[Optional()], choices=[
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro')
    ])
    telefone = StringField('Telefone',
        validators=[Optional(),
            Length(min=10, max=11, message="O telefone deve ter pelo menos 10 caracteres."),
            Regexp(r'^\d{10,11}$', message="O telefone deve ter entre 10 e 11 dígitos sem pontos ou traços.")
    ])
    email = EmailField('Email', validators=[Optional(), Email(message="Email inválido.")
    ])
    senha = PasswordField('Senha',
        validators=[Optional(),
            Length(min=8, message="A senha deve ter no mínimo 8 caracteres."),
            Regexp(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$',
                   message="A senha deve ter pelo menos uma letra, um número e um caractere especial.")
    ])
    endereco = StringField('Endereço', validators=[Optional()])
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> dict:
        return {
            'genero': self.genero.data,
            'telefone': self.telefone.data,
            'email': self.email.data,
            'senha': self.senha.data,
            'endereco': self.endereco.data
        }
