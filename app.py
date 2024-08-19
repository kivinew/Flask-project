from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/<name>')
def home(name):
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    return "About Page"

@app.route('/hello/<name>')
def hello(name):
    return f"Hello, {name}!"


if __name__ == '__main__':
    app.run(debug=True)