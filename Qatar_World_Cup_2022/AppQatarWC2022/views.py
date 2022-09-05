from django.shortcuts import render

from .models import *
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def promo_codes(request):
    context = {'promo_codes': PromoCode.objects.all()}
    return render(request,"promo_codes.html",context)

def users(request):
    context = {'users': User.objects.all()}
    return render(request,"users.html",context)

def filtered_users(request):
    if request.GET["first_name"]:
        user_name = request.GET["first_name"]
        users = User.objects.filter(first_name=user_name)
        return render(request,"filtered_users.html",{"users":users})
    else:
        return render(request,"users.html")

def player_cards(request):
    context = {'player_cards': PlayerCard.objects.all()}
    return render(request,"player_cards.html",context)

def user_registration(request):
    if request.method == 'POST':
        first_name = request.POST["user_first_name"]
        last_name = request.POST["user_last_name"]
        birthdate = request.POST["user_birthdate"]
        email = request.POST["user_email"]
        country = request.POST["user_country"]
        user = User(first_name = first_name,last_name = last_name,birthdate = birthdate,country = country,email = email)
        user.save()
        context = {'users': User.objects.all()}
        return render(request,"users.html",context)
    else:  
        return render(request,"user_registration.html")