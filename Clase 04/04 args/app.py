from flask import Flask, request


app = Flask(__name__)


@app.route('/query-example')
def query_example():
    language = request.args.get('language') # Si el valor no existe, coloca None

    framework = request.args['framework']  # Si el valor no existe, levanta una excepción

    website = request.args.get('website', "localhost")  # Si el valor no existe, utiliza el valor por default

    return '''
              <h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)

if __name__ == '__main__':
    app.run(debug=True)
