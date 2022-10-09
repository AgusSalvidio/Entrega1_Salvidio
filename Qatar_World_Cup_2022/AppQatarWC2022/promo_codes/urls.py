from django.urls import path

from AppQatarWC2022.promo_codes.views import promo_codes

urlpatterns = [
    path('promo_codes/',promo_codes,name='promo_codes'),
]