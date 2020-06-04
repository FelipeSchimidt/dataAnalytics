from flask import Flask, jsonify, request
import pyrebase
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
config = {
    "apiKey": os.getenv("ENV_API_KEY"),
    "authDomain": os.getenv("ENV_AUTH_DOMAIN"),
    "databaseURL": os.getenv("ENV_DATABASE_URL"),
    "storageBucket": os.getenv("ENV_STORAGE_BUCKET")
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

app = Flask('__name__')

pessoal = [
    {
        "id": 1,
        "first_name": "Felipe",
        "last_name": "Santos",
        "function": "Analista de pessoal"
    },
    {
        "id": 2,
        "first_name": "Lizyane",
        "last_name": "Santos",
        "function": "professora"
    }, {
        "id": 3,
        "first_name": "Joene",
        "last_name": "Santos",
        "function": "psicologa"
    }, {
        "id": 4,
        "first_name": "Valquiria",
        "last_name": "Santos",
        "function": "Contas a pagar"
    }, {
        "id": 5,
        "first_name": "Alfredo",
        "last_name": "Santos",
        "function": "Dieretor Administrativo"
    }
]


@app.route('/', methods=['GET'])
def index():
    # datas = [data for data in pessoal]
    return jsonify(pessoal), 200


@app.route('/person/functions/<string:function>', methods=['GET'])
def person_per_function(function):
    functions = [func for func in pessoal if func['function'] == function]
    return jsonify(functions), 200


@app.route('/person/id/<int:id>', methods=['GET'])
def person_per_id(id):
    for pessoas in pessoal:
        if pessoas['id'] == id:
            return jsonify(pessoas)


@app.route('/person/id/<int:id>', methods=['PUT'])
def update_function(id):
    for pessoas in pessoal:
        if pessoas['id'] == id:
            pessoas['function'] = request.get_json().get('function')

            return jsonify(pessoas), 200

    return jsonify({'error': 'registro não encontrado'}), 404


@app.route('/person/new', methods=['POST'])
def new_person():
    novo = request.get_json()
    pessoal.append(novo)

    return jsonify(novo), 201


@app.route('/person/id/<int:id>', methods=['DELETE'])
def delete_person(id):
    for pessoas in pessoal:
        if pessoas['id'] == id:
            pessoal.pop(id-1)
            return jsonify({'message': 'Pessoa deletada'}), 200

    return jsonify({'error': 'Pessoa não encontrada'}), 404


@app.route('/stations/', methods=['GET'])
def stations():
    dict_station = {}
    stations = db.child('stations').get()
    for station in stations.each():
        dict_station.items(station)

    return jsonify(dict_station)


if __name__ == '__main__':
    app.run(Debug=True)
