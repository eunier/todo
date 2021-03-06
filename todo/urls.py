from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_new_todo, name='add'),
    path('complete/<todo_id>', views.complete_todo, name='complete'),
    path('delete', views.delete_todo, name='delete'),
    path('delete-all', views.delete_all, name='delete_all'),
]
