import json
from datetime import datetime

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from polls.models import Question


def index(request):
    return HttpResponse("Hola! Estás en el index de polls.")

@csrf_exempt
def questions(request):
    if request.method == "GET":
        # Serializa la lista de objectos en un Json
        data = serializers.serialize("json", Question.objects.all())
        return JsonResponse(data, safe=False)
    if request.method == "POST":
        # Convierte el body en un dict
        body = json.loads(request.body.decode("utf-8"))
        pub_date_str = body["pub_date"]
        pub_date = datetime.strptime(pub_date_str, "%Y-%m-%d")  # Analiza la cadena en un objeto datetime

        new_question = Question.objects.create(
            question_text=body["question_text"],
            pub_date=pub_date,
            email=body["email"]
        )
        # Parsea el objeto de la bdd a json
        data = serializers.serialize('json', [new_question])
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)


