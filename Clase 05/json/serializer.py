import json

datos_JSON =  """
{
    "tamano": "mediana",
    "precio": 15.67,
    "toppings": ["champinones", "queso extra", "pepperoni", "albahaca"],
    "cliente": {
        "nombre": "Jane Doe",
        "telefono": "455-344-234",
        "correo": "janedoe@email.com"
    }
}
"""

datos_diccionario = json.loads(datos_JSON)
print(type(datos_diccionario))
# print(json.loads(datos_diccionario))

print(datos_diccionario["tamano"])
print(datos_diccionario["precio"])
print(datos_diccionario["toppings"])
print(datos_diccionario["cliente"])