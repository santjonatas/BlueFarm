from flask import current_app
from app.domain.entities.cargo_entity import CargoEntity
from app.domain.entities.departamento_entity import DepartamentoEntity
from app.domain.forms.common.base_form import BaseForm
from wtforms import SelectField, StringField, PasswordField, DateField, DecimalField, EmailField, IntegerField, FileField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange, Length, Regexp, Email
from flask_wtf.file import FileAllowed

class AddProdutoForm(BaseForm):
    nome = StringField('Nome',
        validators=[DataRequired(),
            Length(min=2, message="O nome deve ter pelo menos 2 caracteres.")
    ])
    descricao = StringField('Descrição',
        validators=[DataRequired(),
            Length(min=2, max=255, message="A descrição deve ter pelo menos 2 caracteres.")
    ])
    preco = DecimalField('Preço',
        validators=[DataRequired(),
            NumberRange(min=1.00, message="O preço deve ter pelo menos 1 real.")
    ])
    quantidade_disponivel = IntegerField('Quantidade disponível',
        validators=[DataRequired()
    ])
    nome_insumo = StringField('Nome do Insumo',
        validators=[DataRequired(),
            Length(min=2, message="O nome do insumo deve ter pelo menos 2 caracteres.")
    ])
    descricao_insumo = StringField('Descrição do Insumo',
        validators=[DataRequired(),
            Length(min=2, max=255, message="A descrição do insumo deve ter pelo menos 2 caracteres.")
    ])
    preco_insumo = DecimalField('Preço do Insumo',
        validators=[DataRequired(),
            NumberRange(min=1.00, message="O preço do insumo deve ter pelo menos 1 real.")
    ])
    quantidade_disponivel_insumo = IntegerField('Quantidade disponível de insumos',
        validators=[DataRequired()
    ])
    comprado_em = DateField('Data de Compra',
        validators=[DataRequired()]
    )
    file = FileField('Upload Image', validators=[ 
        DataRequired(), 
        FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Somente imagens!')
    ])
    submit = SubmitField('Upload')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self) -> dict:
        return {
            'nome': self.nome.data,
            'descricao': self.descricao.data,
            'preco': self.preco.data,
            'quantidade_disponivel': self.quantidade_disponivel.data,
            'nome_insumo': self.nome_insumo.data,
            'descricao_insumo': self.descricao_insumo.data,
            'preco_insumo': self.preco_insumo.data,
            'quantidade_disponivel_insumo': self.quantidade_disponivel_insumo.data,
            'comprado_em': self.comprado_em.data
        }
