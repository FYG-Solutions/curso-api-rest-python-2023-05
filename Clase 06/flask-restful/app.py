from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

todo_list = [
    {
        "id": 1,
        "value": "Finish mi TODO app"
    },
    {
        "id": 2,
        "value": "Add a POST method to my TODO app"
    }
]


class HelloWorld(Resource):
    def get(self):  # Obtener información
        return {'hello': 'world'}



class TodoSimple(Resource):
    """
    CRUD sencillo para crear API REST mediante un ID
    Para más información sobre flask-restful consulte https://flask-restful.readthedocs.io/en/latest/
    TODO: Implementar el método PUT para actualizar una entidad completa mediante su ID
        PUT {{host}}/todos/<int:id>
    TODO: Implementar el método DELETE para elimintar una entidad completa mediante su ID
        DELETE {{host}}/todos/<int:id>
    """
    def get(self, id):
        """
        Esta función pretende buscar un elemento en particular de la lista de TODO's mediante su ID
            Debemos rescatar el id de la petición
            Buscar ese id en el atributo id de cada objeto de la lista de elementos
            Si encuentro la entidad que tenga el mismo ID, le regreso al cliente
            Si no lo encuentro, regresamos el mensaje de no encontrado
        """
        # Buscar en la lista de objetos
        # Itera cada elemento y si encuentras el ID, lo regresas
        # for item in todo_list:
        #     if item["id"] == id:
        #         return item
        
        found_todo = next((item for item in todo_list if item["id"] == id), None)
        
        if found_todo is None:
            return {'message': "No se encontro el TODO con id: " + str(id)}
        
        return found_todo


class TodoSimpleList(Resource):
    """
    Recurso para gestionar peticiones genéricas y adición de entidades 
    """
    def get(self):
        return {'data': todo_list}
    
    def post(self):
        # Parser
        # Doc: https://flask-restful.readthedocs.io/en/latest/reqparse.html
        parser = reqparse.RequestParser()
        # Look only in the POST body
        parser.add_argument('id', type=int, help='El campo "id" es obligatorio', required=True)
        parser.add_argument('value', type=str, help='El campo "value" es obligatorio', required=True)
        args = parser.parse_args()
        # Obtención de datos
        id = args.get('id')
        value = args.get('value')
        # Creamos el elemento y lo agregamos al todo-list
        new_item =  {"id":id, "value":value}
        # TODO: Agregar una validación para que sólo existan id's únicos
        todo_list.append(new_item)
        return new_item


api.add_resource(HelloWorld, '/')
api.add_resource(TodoSimpleList, '/todos/')
api.add_resource(TodoSimple, '/todos/<int:id>/')

if __name__ == '__main__':
    app.run(debug=True)
