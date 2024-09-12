"""Adicionando tabela departamentos e ajustando chaves estrangeiras

Revision ID: ed127fdaf3ec
Revises: 
Create Date: 2024-09-11 23:53:58.377302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed127fdaf3ec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    schema = os.getenv('SQLALCHEMY_DATABASE_SCHEMA', 'bluefarm')

    # Criação da tabela base
    op.create_table(
        'pessoas',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('nome', sa.Text(), nullable=False),
        sa.Column('data_nascimento', sa.Date(), nullable=False),
        sa.Column('cpf', sa.String(100), nullable=False, unique=True),
        sa.Column('genero', sa.String(25), nullable=True),
        sa.Column('telefone', sa.String(11), nullable=True, unique=True),
        sa.Column('email', sa.String(100), nullable=True, unique=True),
        sa.Column('endereco', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )

    op.create_table(
        'usuarios',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_pessoa', sa.Integer(), nullable=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('senha', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['id_pessoa'], ['pessoas.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )

    op.create_table(
        'niveis',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('acesso', sa.Boolean(), nullable=False, default=False),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )

    op.create_table(
        'cargos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_nivel', sa.Integer(), nullable=True),
        sa.Column('funcao', sa.String(50), nullable=False),
        sa.Column('salario', sa.Numeric(10, 2), nullable=False),
        sa.ForeignKeyConstraint(['id_nivel'], ['niveis.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )

    op.create_table(
        'funcionarios',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_usuario', sa.Integer(), nullable=True),
        sa.Column('id_cargo', sa.Integer(), nullable=True),
        sa.Column('data_admissao', sa.Date(), nullable=False),
        sa.ForeignKeyConstraint(['id_usuario'], ['usuarios.id']),
        sa.ForeignKeyConstraint(['id_cargo'], ['cargos.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )

    op.create_table(
        'departamentos',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('area', sa.String(50), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )

    op.create_table(
        'administradores',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_funcionario', sa.Integer(), nullable=True),
        sa.Column('id_departamento', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['id_funcionario'], ['funcionarios.id']),
        sa.ForeignKeyConstraint(['id_departamento'], ['departamentos.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )

    op.create_table(
        'operadores',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('id_funcionario', sa.Integer(), nullable=True),
        sa.Column('id_supervisor', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['id_funcionario'], ['funcionarios.id']),
        sa.ForeignKeyConstraint(['id_supervisor'], ['administradores.id']),
        sa.PrimaryKeyConstraint('id'),
        schema=schema
    )


def downgrade():
    pass
