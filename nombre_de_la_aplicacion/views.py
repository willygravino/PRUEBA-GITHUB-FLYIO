from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'plantillas/about.html')


def about(request):
    return HttpResponse("Esta es la página Acerca de")