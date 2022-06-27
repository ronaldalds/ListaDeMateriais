from flask_wtf import FlaskForm
from wtforms import SubmitField, validators, FileField


class FileForm(FlaskForm):
    file = FileField('Arquivo do Projeto ',[validators.DataRequired()])
    salvar = SubmitField('Salvar')