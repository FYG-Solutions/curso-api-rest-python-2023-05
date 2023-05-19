from flask import Flask


app = Flask(__name__)

@app.route('/hello/<string:nombre>', methods=["GET", "POST"])
def hello_nombre(nombre):
    return f'¡Hola, {nombre}!'


@app.route('/hello/<string:nombre>/<int:edad>')
def hello_nombre_edad(nombre, edad):
    return f'¡Hola, {nombre}, tienes {edad} años cumplidos!'


if __name__ == '__main__':
    app.run(debug=True)
