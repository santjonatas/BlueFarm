from flask import current_app
from app.domain.entities.cargo_entity import CargoEntity
from app.domain.entities.departamento_entity import DepartamentoEntity
from app.domain.forms.common.base_form import BaseForm
from wtforms import SelectField, StringField, PasswordField, DateField, DecimalField, EmailField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email

class RegisterAdmForm(BaseForm):
    nome = StringField('Nome',
        validators=[DataRequired(),
            Length(min=2, message="O nome deve ter pelo menos 2 caracteres.")
    ])
    data_nascimento = DateField('Data de nascimento',
        validators=[DataRequired()
    ])
    cpf = StringField('CPF',
        validators=[DataRequired(),
                    Length(min=11, max=11, message="O CPF deve ter 11 caracteres."),
            Regexp(r'^\d{11}$', message="O CPF deve ter 11 dígitos sem pontos ou traços.")
    ])
    genero = SelectField('Gênero', validators=[DataRequired()], choices=[
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro')
    ])
    telefone = StringField('Telefone',
        validators=[DataRequired(),
            Length(min=10, max=11, message="O telefone deve ter pelo menos 10 caracteres."),
            Regexp(r'^\d{10,11}$', message="O telefone deve ter entre 10 e 11 dígitos sem pontos ou traços.")
    ])
    email = EmailField('Email', validators=[DataRequired(), Email(message="Email inválido.")
    ])
    username = StringField('Username',
        validators=[DataRequired(),
            Length(min=4, max=20, message="O username deve ter entre 4 e 20 caracteres."),
            Regexp(r'^\w+$', message="O username deve conter apenas letras, números e underscores.")
    ])
    senha = PasswordField(
    'Senha',
    validators=[
        DataRequired(),
        Length(min=8, message="A senha deve ter no mínimo 8 caracteres."),
        Regexp(
            r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$',
            message="A senha deve ter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial."
            )
        ]
    )
    endereco = StringField('Endereço', validators=[DataRequired()])
    data_admissao = DateField('Data de admissão', validators=[DataRequired()])
    cargo = SelectField('Cargo', coerce=str, validators=[DataRequired()])
    departamento = SelectField('Departamento', coerce=str, validators=[DataRequired()])
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        with current_app.app_context():
            self.cargo.choices = [(cargo.id, cargo.funcao) for cargo in CargoEntity.query.all()]
            self.departamento.choices = [(departamento.id, departamento.area) for departamento in DepartamentoEntity.query.all()]

    def to_dict(self) -> dict:
        return {
            'nome': self.nome.data,
            'data_nascimento': self.data_nascimento.data,
            'cpf': self.cpf.data,
            'genero': self.genero.data,
            'telefone': self.telefone.data,
            'email': self.email.data,
            'username': self.username.data,
            'senha': self.senha.data,
            'endereco': self.endereco.data,
            'data_admissao': self.data_admissao.data,
            'cargo': self.cargo.data,
            'departamento': self.departamento.data,
        }
