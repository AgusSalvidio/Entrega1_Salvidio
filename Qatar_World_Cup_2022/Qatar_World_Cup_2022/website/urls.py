from django.urls import path

from Qatar_World_Cup_2022.website.views import home

from AppQatarWC2022.users.urls  import urlpatterns as user_urls

urlpatterns = [
    path('home', home, name="home"),
    path('', home, name="home"),
]

urlpatterns += user_urls

