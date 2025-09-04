from django.urls import path, re_path, include
import hello_world.views as view

temppatterns = [
    path("", view.product_info),
    path("price", view.product_price),
    path("count", view.product_count)
]

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", view.index),
    path("sayhello", view.sayHello),
    path("product/", include(temppatterns)),
    path("user", view.user),
    path("user/<str:name>", view.user),
    path("agent", view.agent),
    path("hello", view.hello_world),
    path("about", view.hello_world),
    path("contact", view.contact),
    re_path(r"^about", view.about_us),
]