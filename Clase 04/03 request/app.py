from flask import Flask, request


app = Flask(__name__)


@app.route('/hello', methods=["GET", "POST"])
def hello_world():
    print(request.method)
    return f'Peticion recibida por {request.method}'


if __name__ == '__main__':
    app.run(debug=True)
