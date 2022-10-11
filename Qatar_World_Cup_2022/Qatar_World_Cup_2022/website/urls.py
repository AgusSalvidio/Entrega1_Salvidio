from django.urls import path

from Qatar_World_Cup_2022.website.views import home,about,pages

from AppQatarWC2022.users.urls  import urlpatterns as user_urls

urlpatterns = [
    path('home/', home, name="home"),
    path('about/',about,name='about'),
    path('pages/',pages,name='pages'),
    path('', home, name="home"),
]

urlpatterns += user_urls

