from flask import Flask

app = Flask('__name__')


@app.route('/')
def home():
    return 'micro servidor ativo'


if __name__ == '__main__':
    app.run(Debug=True)
