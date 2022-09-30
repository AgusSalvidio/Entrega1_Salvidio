"""Qatar_World_Cup_2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from AppQatarWC2022.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',home,name='home'),
    path('promo_codes/',promo_codes,name='promo_codes'),
    path("promo_code_registration", promo_code_registration, name="promo_code_registration"),
    path("promo_code_update/<id>", promo_code_update, name="promo_code_update"),
    path("promo_code_unregistration/<id>", promo_code_unregistration, name="promo_code_unregistration"),
    path('player_stickers/',player_stickers,name='player_stickers'),
    path("player_sticker_registration/", player_sticker_registration, name="player_sticker_registration"),
    path("player_sticker_update/<id>", player_sticker_update, name="player_sticker_update"),
    path("player_sticker_unregistration/<id>", player_sticker_unregistration, name="player_sticker_unregistration"),
    path("my_album", my_album, name="my_album"),
]
