from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_todo_list, name='get_todo_list'),
    path('add', views.add_new_item, name='add'),
    path('update/<int:item_id>', views.update_item, name='update'),
]