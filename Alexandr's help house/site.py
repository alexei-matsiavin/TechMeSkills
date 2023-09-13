from flask import Flask
from flask import render_template
from flask import request
import db
import os

template_dir = os.path.abspath("D:/python/TechMeSkills/Alexandr's help house/templates")
app = Flask(__name__, template_folder=template_dir)


@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/donation', methods=['GET', 'POST'])
def donation():
    if request.method == 'POST':
        name = request.form.get('name')
        characteristics = request.form.get('description')
        amount = request.form.get('amount')
        db.record(name, characteristics, amount)
        return render_template('donation_thk.html')
    else:
        return render_template('donation.html')


@app.route('/help', methods=['GET', 'POST'])
def page_search():
    if request.method == 'GET' and request.args.get('search'):
        search = request.args.get('search')
        result = db.search(search)
        if result:
            template_context = dict(Text="Вещь забронирована")
            return render_template('help_result.html', **template_context)
        else:
            template_context = dict(Text="К сожалению такой вещи нет")
            return render_template('help_result.html', **template_context)
    else:
        return render_template('help.html')


if __name__ == '__main__':
    app.run()
