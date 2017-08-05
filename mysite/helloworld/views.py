from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Add_Word

def index(request):
    data_list = Add_Word.objects.all()
    context = {
        'lists': data_list,
    }
    return render(request, 'helloworld/index.html', context)
