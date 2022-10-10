from django.urls import path

from AppQatarWC2022.album.views import my_album,qualified_countries,update_current_album_page

urlpatterns = [
    path("my_album/", my_album, name="my_album"),
    path("qualified_countries/", qualified_countries, name="qualified_countries"),
    path("update_current_album_page/<country_name>/", update_current_album_page, name="update_current_album_page"),
]

  