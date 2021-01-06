# from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judul':'Home',
        'nav': [
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'index.html', context)


    # judul = "<h1>Ini adalah judul</h1>"
    # body = "<h2>Ini adalah isi dari posts</h2>"

    # return HttpResponse(judul + body)

