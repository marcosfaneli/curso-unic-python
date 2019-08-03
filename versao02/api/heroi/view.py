from flask import Blueprint
from flask import jsonify
from flask import request
from heroi.model import herois
from heroi.model import incluir_heroi
from heroi.model import remover_heroi

heroi = Blueprint('heroi', __name__)

@heroi.route('/heroi', methods=['GET'])
def listar():
    return jsonify(herois), 200


@heroi.route('/heroi', methods=['POST'])
def incluir():
    incluir_heroi(request.json['heroi'])

    return 'ok', 200


@heroi.route('/heroi/<id>', methods=['DELETE'])
def remover(id):
    remover_heroi(int(id))

    return 'ok', 200