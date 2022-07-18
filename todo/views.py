from django.shortcuts import render
from .models import Todo


# Create your views here.

def todo(request):
    
    todos = None
    if request.user.is_authenticated:
        todos = Todo.objects.filter(user=request.user)
        for todo in todos:
            print(f'{todo.id} {todo.title}')
    
    return render(request, './todo/todo.html', {'todos' : todos})