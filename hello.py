from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!!!</h1>'

""" Descobrir porque esse codigo nao esta funcionando """
# @app.route('/request')
# def request():
#     user_agent = request.headers.get('User-Agent')
#     return '<p>Your browser is {}</p>'.format(user_agent)


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
