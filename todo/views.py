from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
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


def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/update_item.html', context)


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('get_todo_list')