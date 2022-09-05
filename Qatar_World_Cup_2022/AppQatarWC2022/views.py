from django.shortcuts import render

from .models import PromoCode,User,PlayerCard
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def promo_codes(request):
    return render(request,"promo_codes.html")

def users(request):
    return render(request,"users.html")

def player_cards(request):
    return render(request,"player_cards.html")
