from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'judul':'Blog',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/blog/populer','Populer'],
            ['/about','About'],
        ]
    }
    return render(request,'blog/index.html', context)

def populer(request):
    context = {
        'judul':'Populer',
        'nav': [
            ['/blog','Blog'],
            ['/blog/populer','Populer'],
        ]
    }
    return render(request,'blog/index.html', context)

# def populer(request):
#     return HttpResponse('<h1>Ini adalah Blog test URLS</h1>')