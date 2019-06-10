from flask import Flask, render_template, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

from LoginForm import LoginForm
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

SECRET_KEY='uma cadeia aleatória'

app.secret_key = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meu-db.sqlite'
app.config['SQLALCHEMY_TRAK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Usuario(db.Model):
    __tablename__ = 'Usuario'
    username = db.column(db.String(40), primary_key=True)
    password = db.column(db.String(40))

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.username = kwargs.pop('username')
        self.password = generate_password_hash(kwargs.pop('password'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)



@app.route('/login', methods=['GET', 'POST'])
def autenticar_usuario():
    formulario = LoginForm()
    if formulario.validate_on_submit():
        render_template('index.html')

    return render_template('login.html', titulo="Autenticar",form=formulario)

@app.route('/')
def inicio():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
