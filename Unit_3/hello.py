from flask import Flask
from flask import render_template
from flask import request
import db
import os

template_dir = os.path.abspath('D:/python/TechMeSkills/Unit_3/templates')
app = Flask(__name__, template_folder=template_dir)


@app.route('/')
def index():
    return render_template('index.html', name='Oleg')

@app.route('/hello')
def hello_world():
    # name = request.args.get('name')
    return render_template('hello.html')  # f'Hello World!'

@app.route('/example')
def example():
    return render_template('example.html')

@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        name = request.form.get('name')
        amount = request.form.get('amount')
        db.record_(name, amount, 3)
        print(f'name={name}, amount={amount}')
        return
    else:
        template_context = dict(title_name="Donation thing's", form_name='Donation')
        return render_template('donation.html', **template_context)


@app.route('/page', methods=['GET', 'POST'])
def pagedb():
    if request.method == 'POST':
        name = request.form.get('name')
        amount = request.form.get('amount')
        db.record_(name, amount, 3)
        return 'OK, запись произведена'
    else:
        return f"""<html>
            <body>
                <label for="name"> Регистрация пожертвований </label>
                <form action= "" method="POST">
                <p>Пожертвования <input id="name" name="name" size='25' placeholder="Введите наименование товара" autofocus></p> 
                <p>Количество <input id="amount" name ="amount" size='25' placeholder="Введите количество товара" autofocus></p>
                <button type="submit">Пожертвовать</button>
                </form>
                <h1> Регистрация Прошения </h1>
                <button type="submit">Попросить</button>
            </body>
            </html>"""


@app.route('/page_get', methods=['GET', 'POST'])
def page_get():
    if request.method == 'GET':
        name = request.args.get('name')
        amount = request.args.get('amount')
        db.record_(name, amount, 3)
        return 'OK, запись произведена'
    else:
        return f"""<html>
            <body>
                <label for="name"> Регистрация пожертвований </label>
                <form action= "" method="GET">
                <p>Пожертвования <input id="name" name="name" size='25' placeholder="Введите наименование товара" autofocus></p> 
                <p>Количество <input id="amount" name ="amount" size='25' placeholder="Введите количество товара" autofocus></p>
                <button type="submit">Пожертвовать</button>
                </form>
                <h1> Регистрация Прошения </h1>
                <button type="submit">Попросить</button>
            </body>
            </html>"""


@app.route('/page_search', methods=['GET', 'POST'])
def page_search():
    if request.method == 'POST':
        name = request.form.get('name')
        amount = request.form.get('amount')
        db.record_(name, amount, 3)
        return 'OK, запись произведена'
    elif request.method == 'GET' and not request.args.get('search') is None:
        # elif request.method == 'GET' and request.args.get('search') != None:
        search = request.args.get('search')
        result = db.search(search)
        return f'{result}'
    else:
        return f"""<html>
            <body>
                <label for="name"> Регистрация пожертвований </label>
                <form action= "" method="POST">
                <p>Пожертвования <input id="name" name="name" size='25' placeholder="Введите наименование товара" autofocus></p> 
                <p>Количество <input id="amount" name ="amount" size='25' placeholder="Введите количество товара" autofocus></p>
                <button type="submit">Пожертвовать</button>
                </form>
                <h1> Регистрация Прошения </h1>
                <form action= "" method="GET">
                <p>Что просим <input id="name" name="search" size='25' placeholder="Введите наименование товара" autofocus></p> 
                <button type="submit">Попросить</button>
                </form>
                
            </body>
            </html>"""


# <button type="submit">Пожертвования</button> <input id="name" placeholder="Введите наименование" autofocus>


@app.route('/name')
def get_recipe():
    return render_template('hi.html', user=user)


if __name__ == '__main__':
    app.run()
