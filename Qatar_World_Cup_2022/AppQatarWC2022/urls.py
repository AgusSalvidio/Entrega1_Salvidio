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

urlpatterns = [
    path('',home,name='home'),
    path('player_cards/',player_cards,name='player_cards'),
    path('users/',users,name='users'),
    path('promo_codes/',promo_codes,name='promo_codes'),
    path('user_registration/',user_registration,name='user_registration'),
    path('filtered_users/',filtered_users,name='filtered_users'),
    path("player_card_registration/", player_card_registration, name="player_card_registration"),
    path("promo_code_registration", promo_code_registration, name="promo_code_registration"),
    path("delete_code/<id>", delete_code, name="delete_code"),
    path("promo_code_update/<id>", promo_code_update, name="promo_code_update"),
    path("player_card_detele/<id>", player_card_delete, name="player_card_delete"),
    path("player_card_update/<id>", player_card_update, name="player_card_update"),
    path("user_delete/<id>", user_delete, name="user_delete"),
    path("user_update/<id>", user_update, name="user_update" ),
]
