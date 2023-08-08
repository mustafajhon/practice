from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks = ['Sahil', 'Mustafa', 'Yousof', 'Naib', 'Ali']
a = 21
b = 33


def index(request):
    return render(request, 'task/task.html', {
        'tasks': tasks,
        'total': f'{a + b}'
    })


def add(request):
    return render(request, 'task/add.html')
