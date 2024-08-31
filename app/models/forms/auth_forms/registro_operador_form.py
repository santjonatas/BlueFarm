from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, DecimalField, EmailField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email

class RegistroOperadorForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, message="O nome deve ter pelo menos 2 caracteres.")])
    data_nascimento = DateField('Data de nascimento', validators=[DataRequired()])
    cpf = StringField('CPF', validators=[DataRequired(), Length(min=11, max=11, message="O CPF deve ter 11 dígitos sem pontos ou traços."), Regexp(r'^\d{11}$', message="O CPF deve ter 11 dígitos sem pontos ou traços.")])
    genero = StringField('Gênero', validators=[DataRequired(), Length(max=25, message="O gênero deve ter no máximo 25 caracteres.")])
    telefone = StringField('Telefone', validators=[DataRequired(), Length(min=10, max=11, message="O telefone deve ter entre 10 e 11 dígitos sem pontos ou traços."), Regexp(r'^\d{10,11}$', message="O telefone deve ter entre 10 e 11 dígitos sem pontos ou traços.")])
    email = EmailField('Email', validators=[DataRequired(), Email(message="Email inválido."),  Length(max=100, message="O email deve ter no máximo 100 caracteres.")])
    endereco = StringField('Endereço', validators=[DataRequired()])

    data_admissao = DateField('Data de admissão', validators=[DataRequired()])
    cargo = StringField('Cargo', validators=[DataRequired(),  Length(max=25, message="O cargo deve ter no máximo 25 caracteres.")])
    salario = DecimalField('Salário', validators=[DataRequired(), NumberRange(min=0, message="O salário deve ser um valor positivo.")], places=2)
    data_demissao = DateField('Data de demissão', validators=[Optional()])

    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=50, message="O username deve ter entre 4 e 20 caracteres."), Regexp(r'^\w+$', message="O username deve conter apenas letras, números e underscores.")])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=8, message="A senha deve ter no mínimo 8 caracteres."), Regexp(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$', message="A senha deve ter pelo menos uma letra, um número e um caractere especial.")])
    permissao = StringField('Permissão', validators=[DataRequired(), Length(max=15, message="A permissão deve ter no máximo 15 caracteres.")])

    area_operacao = StringField('Área de operação', validators=[DataRequired(), Length(max=50, message="A área de operação deve ter no máximo 50 caracteres.")])
    supervisor_direto = StringField('Supervisor direto', validators=[Optional(), Length(max=50, message="O supervisor direto deve ter no máximo 50 caracteres.")])


    @property
    def to_dict(self) -> dict:
        return {
            "nome": self.nome.data,
            "data_nascimento": self.data_nascimento.data,
            "cpf": self.cpf.data,
            "genero": self.genero.data,
            "telefone": self.telefone.data,
            "email": self.email.data,
            "endereco": self.endereco.data,
            "data_admissao": self.data_admissao.data,
            "cargo": self.cargo.data,
            "salario": str(self.salario.data),
            "data_demissao": self.data_demissao.data,
            "username": self.username.data,
            "senha": self.senha.data,
            "permissao": self.permissao.data,
            "area_operacao": self.area_operacao.data,
            "supervisor_direto": self.supervisor_direto.data
        }