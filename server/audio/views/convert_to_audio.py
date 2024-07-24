from django.http import JsonResponse

def sayHello(request):
    return JsonResponse({"msg": "Hello World"})