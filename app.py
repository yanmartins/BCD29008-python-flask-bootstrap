from flask import Flask, render_template, flash, redirect, url_for

app = Flask(__name__)

SECRET_KEY='uma cadeia aleatória'

app.secret_key = SECRET_KEY

@app.route('/login')
def autenticar_usuario():
    return render_template('login.html')

@app.route('/')
def inicio():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
