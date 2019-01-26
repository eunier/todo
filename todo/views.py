from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .form import TodoForm
from .models import Todo


# Create your views here.
def index(request):
    mytodo = Todo.objects.order_by('id')
    form = TodoForm()
    context = {
        'mytodo': mytodo,
        'form': form
    }
    return render(request, 'todo/index.html', context)


@require_POST
def add_new_todo(request):
    form = TodoForm(request.POST)

    if form.is_valid():
        my_new_todo = Todo(todotext=request.POST['text'])
        my_new_todo.save()

    return redirect('index')
