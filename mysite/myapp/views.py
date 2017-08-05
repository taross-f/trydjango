from django.http import HttpResponse

def myapp_index(request):
    return HttpResponse('Hello world')