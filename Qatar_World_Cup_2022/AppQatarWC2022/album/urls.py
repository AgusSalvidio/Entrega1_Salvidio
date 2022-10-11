from django.urls import path

from AppQatarWC2022.album.views import my_album,qualified_countries,update_current_album_page,next_page,previous_page,glue_sticker

urlpatterns = [
    path("my_album/", my_album, name="my_album"),
    path("qualified_countries/", qualified_countries, name="qualified_countries"),
    path("update_current_album_page/<country_name>/", update_current_album_page, name="update_current_album_page"),
    path("next_page/", next_page, name="next_page"),
    path("previous_page/", previous_page, name="previous_page"),
    path("glue_sticker/<id>/", glue_sticker, name="glue_sticker"),
]

  