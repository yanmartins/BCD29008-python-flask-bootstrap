from flask_wtf import FlaskForm
from wtforms import SelectField, PasswordField, BooleanField, SubmitField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Nome de Usuario', validators=[DataRequired("Campo obrigatório")])
    password = PasswordField('Senha', validators=[DataRequired("Campo obrigatório")])
    submit = SubmitField('Entrar')

