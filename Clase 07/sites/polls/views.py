from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola! Estás en el index de polls.")
