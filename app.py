from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

@app.route('/<name>')
def hello(name):
    return render_template('index.html', name=name)

@app.route('/kivinew')
def kivinew():
    return render_template('kivinew.html')

if __name__ == '__main__':
    app.run(debug=True)
