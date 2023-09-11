from flask import Flask, render_template, request, redirect

app = Flask(__name__)


users = {
    'admin': 'password',
    'alvaro': 'pass123',
    'buitrete': 'buitre',
    'alejandro': 'sapo',
    'joha': 'clave123'
}


@app.route('/login', methods=['GET', 'POST'])
def login():
    # comment
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            return redirect('/dashboard')
        else:
            message = 'Nombre de usuario o contraseña incorrectos'

        return render_template('login.html', message=message)

    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    return '¡Bienvenido al panel de control!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
