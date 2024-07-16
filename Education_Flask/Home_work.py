from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('template_shop.html')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html')


@app.route('/jacket')
def jacket():
    return render_template('jacket.html')


@app.route('/trousers')
def trousers():
    return render_template('trousers.html')


@app.route('/sweater')
def sweater():
    return render_template('sweater.html')


if __name__ == '__main__':
    app.run(debug=True)
