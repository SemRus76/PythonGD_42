# from django.shortcuts import render
# from django.http import HttpResponse, HttpRequest, JsonResponse
import django.http as http


def index(request : http.HttpRequest):
    user_agent = request.META["HTTP_USER_AGENT"]
    user_host = request.META["REMOTE_ADDR"]
    method = request.META["REQUEST_METHOD"]
    response = http.HttpResponse()
    response.write(f"<h1>Это страница исходная</h1>"
                   f"<a href={"hello"}>Перейти на страницу Hello</a>"
                   f"</br>"
                   f"User Agent: {user_agent}"
                   f"</br>"
                   f"User Host: {user_host}"
                   f"</br>"
                   f"User method: {method}"
                   f"</br>"
                   f"<a href={"about"}>Перейти на страницу About</a>"
                   f"</br>"
                   f"<a href={"product"}>Перейти на страницу Product</a>"
                   f"</br>"
                   f"<a href={"user"}>Перейти на страницу User</a>")
    # response.status_code = 201
    # http.HttpResponse
    response.headers["content-type"] = "text/html; charset=utf-8"
    return response

def user(request: http.HttpRequest, name: str = "UNKNOWN"):
    return http.HttpResponse(f"<h1>Hello {name} </h1>"
                        f"<a href={"../"}>Назад</a>")

def agent(request: http.HttpRequest):
    name = request.GET.get("name", "Yandex Market")
    return http.JsonResponse({"name":name, "data":None})

def hello_world(request):
    return http.HttpResponse(f"<h1>Hello World</h1>"
                        f"<a href={"../"}>Назад</a>")

def about_us(request):
    return http.HttpResponse(f"<h1 style='color:red;'>Hello On Our Site!</h1>"
                        f"<a href={"../"}>Назад</a>")

def contact(request):
    return http.HttpResponseRedirect("about")

def product_info(request):
    return http.HttpResponse(f"<h1>Информация о продукте</h1>"
                        f"<a href={"price"}>Цена</a>"
                        f"</br>"
                        f"<a href={"count"}>Количество</a>"
                        f"</br>"
                        f"<a href={".."}>В Самый Назад</a>")

def product_price(request):
    return http.HttpResponse(f"<h1>Информация о цене продукта</h1>"
                        f"<a href={"/product/"}>Информация</a>"
                        f"</br>"
                        f"<a href={"count"}>Количество</a>"
                        f"</br>"
                        f"<a href={".."}>В Начало</a>")

def product_count(request):
    return http.HttpResponse(f"<h1>Информация о кол-ве продукта</h1>"
                        f"<a href={"/product/"}>Информация</a>"
                        f"</br>"
                        f"<a href={"price"}>Цена</a>"
                        f"</br>"
                        f"<a href={".."}>В Назад</a>")

# scheme: схема запроса (http или https)
# body: представляет тело запроса в виде строки байтов
# path: представляет путь запроса
# method: метод запроса (GET, POST, PUT и т.д.)
# encoding: кодировка
# content_type: тип содержимого запроса (значение заголовка CONTENT_TYPE)
#
# GET: объект в виде словаря, который содержит параметры запроса GET
# POST: объект в виде словаря, который содержит параметры запроса POST
# COOKIES: отправленные клиентом куки
# FILES: отправленные клиентом файлы
# META: хранит все доступные заголовки http в виде словаря. Набор заголовков зависит от клиента и сервера, некоторые из них:
# CONTENT_LENGTH: длина содержимого.
# CONTENT_TYPE: MIME-тип запроса.
# HTTP_ACCEPT: типы ответа, которые принимает клиент.
# HTTP_ACCEPT_ENCODING: кодировка, в которой клиент принимает ответ.
# HTTP_ACCEPT_LANGUAGE: язык ответа, который принимает клиент.
# HTTP_HOST: хост сервера.
# HTTP_REFERER: страница, с которой клиент отправил запрос (при ее наличии).
# HTTP_USER_AGENT: юзер-агент или информация о браузере клиента.
# QUERY_STRING: строка запроса.
# REMOTE_ADDR: IP-адрес клиента.
# REMOTE_HOST: имя хоста клиента.
# REMOTE_USER: аутентификационные данные клиента (при наличии)
# REQUEST_METHOD: тип запроса (GET, POST).
# SERVER_NAME: имя хоста сервера.
# SERVER_PORT: порт сервера.
# headers: заголовки запроса в виде словаря
