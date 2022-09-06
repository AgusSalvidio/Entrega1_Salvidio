from django.shortcuts import render
from .forms import *
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

#-------------------------------------------------------------
def player_card_registration(request):
    if request.method=="POST":
        first_name = request.POST["card_first_name"]
        last_name = request.POST["card_last_name"]
        country = request.POST["card_country"]
        birthdate = request.POST["card_birthdate"]
        position = request.POST["card_position"]
        card=PlayerCard(first_name = first_name,last_name = last_name,birthdate = birthdate,country = country,position=position)
        card.save()
        context={"cards": PlayerCard.objects.all()}
        return render(request, "player_cards.html", context)
    else:
        return render(request, "player_card_registration.html")

#------------------------------------------------
def promo_codes_registration(request):
    if request.method=="POST":
        code=request.POST["code"]
        promo_code=PromoCode(code=code)
        promo_code.save()
        context={"code": PromoCode.objects.all()}
        return render(request, "promo_codes.html", context)
    else:
        return render(request, "promo_codes_registration.html")
    
