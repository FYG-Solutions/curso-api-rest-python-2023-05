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
        parsed_data = json.loads(data)  # Serializar el string a json
        return JsonResponse(parsed_data, safe=False)
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
        print(new_question)
        # Parsea el objeto de la bdd a json
        data = serializers.serialize('json', [new_question])
        # Turn the JSON data into a dict and send as JSON response
        return JsonResponse(json.loads(data), safe=False)

@csrf_exempt
def question_detail(request, id):
    if request.method == "GET":
        try:
            question = Question.objects.get(id=id)
            data = serializers.serialize("json", [question])
            return JsonResponse(json.loads(data), safe=False)
        except Question.DoesNotExist:
            return JsonResponse({
                "mensaje": "Pregunta no encontrada"
            }, status=404)
        except Exception:
            return JsonResponse({
                "mensaje": "Opps... Hubo un error..."
            })
    elif request.method == "PUT":
        body = json.loads(request.body.decode("utf-8"))
        try:
            question = Question.objects.get(id=id)
            question.question_text = body.get("question_text", question.question_text)
            pub_date_str = body.get("pub_date", question.pub_date.strftime("%Y-%m-%d"))
            question.pub_date = datetime.strptime(pub_date_str, "%Y-%m-%d")
            question.email = body.get("email", question.email)
            question.save()
            return JsonResponse({"message": "Question updated successfully"})
        except Question.DoesNotExist:
            return JsonResponse({"message": "Question not found"}, status=404)
    elif request.method == "DELETE":
        try:
            question = Question.objects.get(id=id)
            question.delete()
            return JsonResponse(data={},status=204)
        except Question.DoesNotExist:
            return JsonResponse({"message": "Question not found"}, status=404)
    else:
        return JsonResponse({"message": "Method not allowed"}, status=405)