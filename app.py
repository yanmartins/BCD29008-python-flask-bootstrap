from flask import Flask, render_template, flash, redirect, url_for, session
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

    username = db.Column(db.String(40), primary_key=True)
    password = db.Column(db.String(40))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.username = kwargs.pop('username')
        self.password = generate_password_hash(kwargs.pop('password'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


@app.route('/painel')
def mostrar_painel():

    if session.get('autenticado') == True:
        return render_template('painel.html', titulo='Área pessoal')

    return redirect(url_for('autenticar_usuario'))


@app.route('/login', methods=['GET', 'POST'])
def autenticar_usuario():
    formulario = LoginForm()
    if formulario.validate_on_submit():

        user = formulario.username.data
        senha = formulario.password.data

        u = Usuario.query.filter_by(username=user).first()

        if u is not None:
            if u.check_password(senha):

                session['username'] = user
                session['autenticado'] = True

                return redirect(url_for('mostrar_painel'))

    return render_template('login.html', titulo="Autenticar",form=formulario)


@app.route('/logout')
def deslogar_usuario():
    session['autenticado'] = False
    return redirect(url_for('autenticar_usuario'))

@app.route('/')
def inicio():
    return render_template('index.html')


if __name__ == '__main__':
    db.create_all()
    #app.run(debug=True, host='0.0.0.0')
