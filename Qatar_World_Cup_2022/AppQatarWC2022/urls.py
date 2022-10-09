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
    path("element_registration/<str:object_class_name>/<str:form_class_name>", element_registration, name="element_registration"),
    path("element_unregistration/<int:id>/<str:object_class_name>/<str:form_class_name>", element_unregistration, name="element_unregistration"),
    path("element_update/<int:id>/<str:object_class_name>/<str:form_class_name>", element_update, name="element_update"),
    path('promo_codes/',promo_codes,name='promo_codes'),
    path('player_stickers/',player_stickers,name='player_stickers'),
    path("my_album", my_album, name="my_album"),   
]
