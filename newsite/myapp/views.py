from django.shortcuts import render, redirect
from .models import MessageBoard

def myapp_index(request):
    delete_text = request.POST.getlist('delete_text')
    if delete_text:
        MessageBoard.objects.filter(id__in=delete_text).delete()
    msg = request.GET.get('words')
    if msg is None:
        data_list = MessageBoard.objects.order_by('-id')
        contexts = {
            'result_list': data_list,
        }
        return render(request, 'myapp/index.html', contexts)

    message_data = MessageBoard()
    message_data.new_message = msg
    message_data.save()

    data_list = MessageBoard.objects.order_by('-id')
    contexts = {
        'result_list': data_list,
    }
    return render(request, 'myapp/index.html', contexts)
