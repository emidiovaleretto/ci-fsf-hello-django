from django.shortcuts import render

def index(request):
    return render(request, 'todo/todo_list.html')
