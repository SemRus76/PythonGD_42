# from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def index(request):
    response = HttpResponse()
    response.write(f"<h1>Это страница исходная</h1>"
                   f"<a href={"hello"}>Перейти на страницу Hello</a>"
                   f"</br>"
                   f"<a href={"about"}>Перейти на страницу About</a>")
    # response.status_code = 201
    # response.headers["content-type"] = "text/html; charset=utf-8"
    return response

def hello_world(request):
    return HttpResponse(f"<h1>Hello World</h1>"
                        f"<a href={"../"}>Назад</a>")

def about_us(request):
    return HttpResponse(f"<h1 style='color:red;'>Hello On Our Site!</h1>"
                        f"<a href={"../"}>Назад</a>")