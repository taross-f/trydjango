from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import TodoBoard

def myapp_index(request):
    delete_text = request.POST.getlist('delete_text')
    if delete_text:
        TodoBoard.objects.filter(id__in=delete_text).delete()
    msg = request.POST.get('words')
    if msg is None or msg == "":
        data_list = TodoBoard.objects.order_by('-id')
        contexts = {
            'result_list': data_list,
        }
        return render(request, 'myapp/index.html', contexts)

    image_file = request.FILES.get('files')
    message_data = TodoBoard()
    message_data.new_message = msg
    message_data.image_url = image_file
    message_data.save()

    data_list = TodoBoard.objects.order_by('-id')
    contexts = {
        'result_list': data_list,
    }
    return render(request, 'myapp/index.html', contexts)
