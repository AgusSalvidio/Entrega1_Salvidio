from django.urls import path

from AppQatarWC2022.stickers.views import player_stickers

urlpatterns = [
    path('player_stickers/',player_stickers,name='player_stickers'),
]