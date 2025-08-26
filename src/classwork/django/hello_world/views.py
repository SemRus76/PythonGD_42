# from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse(f"<h1>Это страница исходная</h1>"
                        f"<a href={"hello"}>Перейти на страницу Hello</a>")

def hello_world(request):
    return HttpResponse(f"<h1>Hello World</h1>"
                        f"<a href={"../"}>Назад</a>")

