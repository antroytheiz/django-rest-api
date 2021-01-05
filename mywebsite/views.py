# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # judul = "<h1>Ini adalah judul</h1>"
    # body = "<h2>Ini adalah isi dari posts</h2>"

    # return HttpResponse(judul + body)
    return render(request,'index.html')

