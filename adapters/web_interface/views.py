from django.http import HttpResponse


# Create your views here.
def indexV(request):
    return HttpResponse("Hola mundo")
