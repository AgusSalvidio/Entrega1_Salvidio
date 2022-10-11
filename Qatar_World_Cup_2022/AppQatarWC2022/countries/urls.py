from django.urls import path

from AppQatarWC2022.countries.views import countries

urlpatterns = [
    path('countries/',countries,name='countries'),
]