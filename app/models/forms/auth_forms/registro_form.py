from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, DecimalField, EmailField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email

class RegistroForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, message="O nome deve ter pelo menos 2 caracteres.")])
    data_nascimento = DateField('Data de nascimento', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Regexp(r'^\d{11}$', message="O CPF deve ter 11 dígitos sem pontos ou traços.")])
    genero = StringField('Gênero', validators=[DataRequired()])
    telefone = StringField('Telefone', validators=[DataRequired(), Regexp(r'^\d{10,11}$', message="O telefone deve ter entre 10 e 11 dígitos sem pontos ou traços.")])
    email = EmailField('Email', validators=[DataRequired(), Email(message="Email inválido.")])
    endereco = StringField('Endereço', validators=[DataRequired()])

    data_admissao = DateField('Data de admissão', validators=[DataRequired()])
    cargo = StringField('Cargo', validators=[DataRequired()])
    salario = DecimalField('Salário', validators=[DataRequired(), NumberRange(min=0, message="O salário deve ser um valor positivo.")], places=2)
    data_demissao = DateField('Data de demissão', validators=[DataRequired()])

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20, message="O username deve ter entre 4 e 20 caracteres."), Regexp(r'^\w+$', message="O username deve conter apenas letras, números e underscores.")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8, message="A senha deve ter no mínimo 8 caracteres."), Regexp(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', message="A senha deve ter pelo menos uma letra, um número e um caractere especial.")])
    permissao = StringField('Permissão', validators=[DataRequired()])

    permissao_adicional = StringField('Permissão adicional', validators=[Optional()])
    responsavel_por_departamento = StringField('Responsável por departamento', validators=[Optional()])

    area_operacao = StringField('Área de operação', validators=[DataRequired()])
    supervisor_direto = StringField('Supervisor direto', validators=[Optional()])