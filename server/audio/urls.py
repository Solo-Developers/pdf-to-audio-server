from django.urls import path

from audio.views.convert_to_audio import sayHello

urlpatterns = [
    path('convert/',sayHello,name="home"),
]
