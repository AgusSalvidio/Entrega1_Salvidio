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
]
