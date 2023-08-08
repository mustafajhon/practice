from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return HttpResponse('Hello Mustafa')   This is one simple way to write text in the Dom

def index(request):
    return render(request, 'index/index.html')


def index2(request):
    return render(request, 'index/index2.html')
