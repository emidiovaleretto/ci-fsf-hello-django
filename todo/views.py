from django.shortcuts import render, redirect
from .models import *

def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)

def add_new_item(request):

    if request.method == 'POST':
        item_name = request.POST.get('item-name')
        done = 'is-done' in request.POST
        Item.objects.create(name=item_name, done=done)

        return redirect('get_todo_list')

    return render(request, 'todo/add_item.html')