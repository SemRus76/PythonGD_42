from django.urls import path
import hello_world.views as view

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", view.index),
    path("hello", view.hello_world),
]
