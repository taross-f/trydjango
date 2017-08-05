from django.shortcuts import render
from .models import Add_Word

def helloworld_index(request):
    data_list = Add_Word.objects.all()
    context = {
        'lists': data_list,
    }
    return render(request, 'helloworld/index.html', context)
