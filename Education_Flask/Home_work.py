from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('template_shop.html')


@app.route('/trousers')
def trousers():
    trousers_lst = [
        {'model': 'Брюки MELIN BARON', 'size': 40, 'price': 3000},
        {'model': 'Джинсы Gloria Jeans', 'size': 52, 'price': 2000},
        {'model': 'Штаны VOESS', 'size': 35, 'price': 2500}
    ]
    return render_template("trousers.html", trousers_lst=trousers_lst, title='Штаны')


@app.route('/shoes')
def shoes():
    shoes_lst = [
        {'model': 'Reebok Кроссовки CLASSIC LEATHER', 'size': 35, 'price': 5800},
        {'model': 'adidas Кеды ADVANTAGE', 'size': 52, 'price': 3850},
        {'model': 'Cordillero Ботинки Obsidian LTR', 'size': 47, 'price': 3550}
    ]
    return render_template("shoes.html", shoes_lst=shoes_lst, title='Обувь')


@app.route('/jackets')
def jackets():
    jackets_lst = [
        {'model': "Colin's Куртка утепленная", 'size': "46/48", 'price': 3000},
        {'model': 'Urban Fashion for Men Куртка кожаная утепленная', 'size': "54/56", 'price': 9250},
        {'model': r'Lyle & Scott Ветровка Hooded Pocket Jacke', 'size': "36/38", 'price': 7390}
    ]
    return render_template("jackets.html", jackets_lst=jackets_lst, title='Куртки')


if __name__ == '__main__':
    app.run(debug=True)
