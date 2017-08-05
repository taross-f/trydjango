from django.http import HttpResponse
from .models import Add_Word

def index(request):
    data_list = Add_Word.objects.all()
    return HttpResponse(data_list)
