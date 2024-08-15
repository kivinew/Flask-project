from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', title='Home Page', message='Welcome to Flask!')

@app.route('/contacts')
def contacts():
    return render_template('index.html', title='Контакты', message='Звоните:')

@app.route('/contacts')
def contacts():
    return render_template('index.html', title='Контакты', message='Звоните:')

@app.route('/about')
def about():
    return 'This is the ABOUT page'

if __name__ == '__main__':
    app.run(debug=True)