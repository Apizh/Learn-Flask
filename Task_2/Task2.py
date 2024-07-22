from flask import Flask, render_template, request, redirect, make_response, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        # Устанавливаем cookie
        resp = make_response(redirect(url_for('welcome')))
        resp.set_cookie('username', name)
        resp.set_cookie('email', email)  # Можно сохранить электронную почту, если нужно
        return resp

    return render_template('index.html')


@app.route('/welcome')
def welcome():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('index'))
    return render_template('welcome.html', username=username)


@app.route('/logout')
def logout():
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('email', '', expires=0)  # Удаляем email cookie, если нужно
    return resp


if __name__ == '__main__':
    app.run(debug=True)
