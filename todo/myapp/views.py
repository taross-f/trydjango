from django.shortcuts import render, redirect
from .models import TodoBoard

def myapp_index(request):
    delete_text = request.POST.getlist('delete_text')
    if delete_text:
        TodoBoard.objects.filter(id__in=delete_text).delete()
    msg = request.GET.get('words')
    if msg is None or msg == "":
        data_list = TodoBoard.objects.order_by('-id')
        contexts = {
            'result_list': data_list,
        }
        return render(request, 'myapp/index.html', contexts)

    message_data = TodoBoard()
    message_data.new_message = msg
    message_data.save()

    data_list = TodoBoard.objects.order_by('-id')
    contexts = {
        'result_list': data_list,
    }
    return render(request, 'myapp/index.html', contexts)
