from flask import Flask, render_template, flash, redirect, url_for

from LoginForm import LoginForm

app = Flask(__name__)

SECRET_KEY='uma cadeia aleatória'

app.secret_key = SECRET_KEY

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
