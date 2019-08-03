from flask import Flask
from hello.view import hello
from heroi.view import heroi

api = Flask(__name__)

api.register_blueprint(hello)
api.register_blueprint(heroi)

if __name__ == '__main__':
    api.run(debug=True)