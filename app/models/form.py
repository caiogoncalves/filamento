from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField


class EmailForm(FlaskForm):
    nome = StringField("nome", validators=[DataRequired()])
    telefone = StringField("telefone", validators=[DataRequired()])
    email = EmailField("email", validators=[DataRequired(), Email("Email Inválido")])
    #assunto = StringField("assunto", validators=[DataRequired()])
