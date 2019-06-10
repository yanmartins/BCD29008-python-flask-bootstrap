from flask_wtf import FlaskForm
from wtforms import SelectField, PasswordField, BooleanField, SubmitField, StringField


class LoginForm(FlaskForm):
    username = StringField('Nome de Usuario')
    password = PasswordField('Senha')
    submit = SubmitField('Entrar')

