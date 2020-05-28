from flask import Flask, jsonify, request, response

app = Flask('__name__')

dados = [
    {
        "first_name": "Felipe",
        "last_name": "Santos",
        "function": "Analista de dados"
    },
    {
        "first_name": "Lizyane",
        "last_name": "Santos",
        "function": "professora"
    }, {
        "first_name": "Joene",
        "last_name": "Santos",
        "function": "psicologa"
    }, {
        "first_name": "Valquiria",
        "last_name": "Santos",
        "function": "Contas a pagar"
    }, {
        "first_name": "Alfredo",
        "last_name": "Santos",
        "function": "Dieretor Administrativo"
    }
]


@app.route('/', methods=['GET'])
def index():
    datas = [data for data in response.get_json()]
    return 'micro servidor ativo'


@app.route('/new', methods=['POST'])
def new():
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(Debug=True)
