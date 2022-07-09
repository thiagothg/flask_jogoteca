from flask import Flask

app = Flask(__name__)


@app.route('/index')

def hello():
    return '<h1>Hello Mundo<h1>'



app.run()