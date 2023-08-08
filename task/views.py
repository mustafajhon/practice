from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks = ['Sahil', 'Mustafa', 'Yousof', 'Naib', 'Ali']


def index(request):
    return render(request, 'task/task.html', {
        'tasks': tasks
    })
