from django.urls import path

from AppQatarWC2022.stickers.views import player_stickers,logo_stickers,my_stickers

urlpatterns = [
    path('player_stickers/',player_stickers,name='player_stickers'),
    path('logo_stickers/',logo_stickers,name='logo_stickers'),
    path('my_stickers/',my_stickers,name='my_stickers'),
]