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
from AppQatarWC2022.album.urls import urlpatterns as album_urls
from AppQatarWC2022.generic_modals.urls import urlpatterns as generic_modal_urls
from AppQatarWC2022.promo_codes.urls import urlpatterns as promo_code_urls
from AppQatarWC2022.stickers.urls import urlpatterns as sticker_urls
from AppQatarWC2022.users.urls  import urlpatterns as user_urls
from AppQatarWC2022.countries.urls import urlpatterns as country_urls

urlpatterns = album_urls + generic_modal_urls + promo_code_urls + sticker_urls + user_urls + country_urls