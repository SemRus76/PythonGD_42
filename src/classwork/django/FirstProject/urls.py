from django.urls import path, re_path
import hello_world.views as view


urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", view.index),
    path('hello', view.hello_world),
    re_path(r'^about', view.about_us),
    path('user/<str:name>', view.user),
    re_path(r'user/', view.user),
    path("agent", view.agent),
    path("players", view.players_data),
]