from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'blog/index.html')

def populer(request):
    return HttpResponse('<h1>Ini adalah Blog test URLS</h1>')