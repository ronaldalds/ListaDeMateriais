from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, FileField, StringField, PasswordField


class FileForm(FlaskForm):
    file = FileField('Arquivo do Projeto ', [validators.DataRequired()])
    salvar = SubmitField('Salvar')


class UsuariosForm(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    nome = StringField('nome', [validators.DataRequired(), validators.Length(min=1, max=20)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
    criar = SubmitField('Criar')
