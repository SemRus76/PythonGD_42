from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def index(request: HttpRequest):
    user_agent = request.META["HTTP_USER_AGENT"]
    user_addr = request.META["REMOTE_ADDR"]
    request_method = request.META["REQUEST_METHOD"]
    response = HttpResponse()

    response.write(f"<h1>Это страница исходная</h1>"
                        f"<a href={"hello"}> Перейти на страницу Hello</a>"
                        f"</br>"
                        f"<a href={"about"}> Перейти на страницу About</a>"
                        f"</br>"
                        f"<a href={"players"}> Перейти на страницу Players</a>"
                        f"</br>"
                        f"User agent: {user_agent} </br>"
                        f"User host: {user_addr} </br>"
                        f"Request method: {request_method} </br>"
                        f"<a href={"user"}> Перейти на страницу User</a>")

    # response.status_code = 200
    response.headers["content-type"] = "text/html; charset=utf-8"

    return response

def hello_world(request):
    return HttpResponse(f"<h1>Hello World</h1>"
                        f"<a href={"../"}>Назад</a>")

def user(request: HttpRequest, name: str = "UNKNOWN"):
    return HttpResponse(f"<h1>Hello {name}</h1>"
                        f"<a href={"../"}>Назад</a>")

def agent(request: HttpRequest):
    name = request.GET.get("name")
    return JsonResponse({"name" : "name", "data" : "json"})
    # return HttpResponse(f"<h1>Hello {name}</h1>"
    #                     f"<a href={"../"}>Назад</a>")

def about_us(request):
    style = 'color:red;'
    return HttpResponse(f"<h1 style='{style}'>Hello On Our Site!</h1>"
                        f"<a href={"../"}>Назад</a>")

def sayHello(request: HttpRequest):
    print(request.body)
    return request.body

@api_view(['GET','POST'])
def players_data(request):
    name = request.data.get("name")

    return JsonResponse({"helloName":f"{name}"})

