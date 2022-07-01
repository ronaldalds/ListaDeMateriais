from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, FileField, StringField, PasswordField
from math import sqrt
from equipamento import Equipamento

class FileForm(FlaskForm):
    file = FileField('Arquivo do Projeto ', [validators.DataRequired()])
    salvar = SubmitField('Salvar')

    def load_file(self,file):
        return Equipamento(file)

class UsuariosForm(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired(), validators.Length(min=1, max=8)])
    nome = StringField('nome', [validators.DataRequired(), validators.Length(min=1, max=20)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=1, max=100)])
    login = SubmitField('Login')
    criar = SubmitField('Criar')


def meter(x, y):
    cat1 = ((float(x[0])) - (float(y[0]))) * 1852 * 60
    cat2 = ((float(x[1])) - (float(y[1]))) * 1852 * 60
    h = sqrt((cat1 * cat1) + (cat2 * cat2))
    return float(h)
