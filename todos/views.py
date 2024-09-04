from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Todo


def todo_list_old(request):
    nome = 'rodrigo'
    alunos = ['1.Ana','2.Jose', '3.Carlos']
    return render(request, "todos/todo_list.html", {"nome":nome, "lista_alunos":alunos})

def todo_list(request):
    todos = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos})