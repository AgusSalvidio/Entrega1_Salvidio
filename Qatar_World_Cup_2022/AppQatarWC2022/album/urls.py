from django.urls import path

from AppQatarWC2022.album.views import my_album

urlpatterns = [
    path("my_album", my_album, name="my_album"),
]

  