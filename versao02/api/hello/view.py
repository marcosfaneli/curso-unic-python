from flask import Blueprint

hello = Blueprint('hello', __name__)

@hello.route('/')
def ola():
    return '<h1>Olá mundo</h1>'