from django.urls import path, re_path
import hello_world.views as view
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", view.index),
    path("hello", view.hello_world),
    path("about", view.hello_world),
    re_path(r"^about", view.about_us),
]


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
