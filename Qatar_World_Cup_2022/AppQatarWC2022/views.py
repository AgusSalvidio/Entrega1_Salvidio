import code
from django.shortcuts import render
from .models import *
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def users(request):
    context = {'users': User.objects.all()}
    return render(request,"users.html",context)

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

def filtered_users(request):
    if request.GET["first_name"]:
        user_name = request.GET["first_name"]
        users = User.objects.filter(first_name=user_name)
        return render(request,"filtered_users.html",{"users":users})
    else:
        return render(request,"users.html")

def user_delete(request, id):
    user=User.objects.get(id=id)
    user.delete()
    context={"user":User.objects.all()}
    return render (request, "users.html", context)

def user_update(request, id):
    user=User.objects.get(id=id)
    if request.method=="POST":
        user.first_name = request.POST["user_first_name"]
        user.last_name = request.POST["user_last_name"]
        user.birthdate = request.POST["user_birthdate"]
        user.email = request.POST["user_email"]
        user.country = request.POST["user_country"]
        user.save()
        context = {'users': User.objects.all()}
        return render(request,"users.html",context)
    else:
        form=User()
        return render(request, "user_update.html", {"user": user, "form": form})




def player_cards(request):
    context = {'player_cards': PlayerCard.objects.all()}
    return render(request,"player_cards.html",context)

def player_card_registration(request):
    if request.method =="POST":
        first_name = request.POST["card_first_name"]
        last_name = request.POST["card_last_name"]
        country = request.POST["card_country"]
        birthdate = request.POST["card_birthdate"]
        position = request.POST["card_position"]
        player_card = PlayerCard(first_name = first_name,last_name = last_name,birthdate = birthdate,country = country,position=position)
        player_card.save()
        context={"player_cards": PlayerCard.objects.all()}
        return render(request, "player_cards.html", context)
    else:
        return render(request, "player_card_registration.html")

def player_card_delete(request, id):
    player_card=PlayerCard.objects.get(id=id)
    player_card.delete()
    context={"player_cards":PlayerCard.objects.all()}
    return render (request, "player_cards.html", context)

def player_card_update(request, id):
    player_card=PlayerCard.objects.get(id=id)
    if request.method=="POST":
        player_card.first_name = request.POST["card_first_name"]
        player_card.last_name = request.POST["card_last_name"]
        player_card.country = request.POST["card_country"]
        player_card.birthdate = request.POST["card_birthdate"]
        player_card.position = request.POST["card_position"]
        player_card.save()
        context={"player_cards": PlayerCard.objects.all()}
        return render(request, "player_cards.html", context)
    else:
        form=PlayerCard()
        return render(request, "player_card_update.html",{"form": form, "player_card":player_card} )



def promo_codes(request):
    context = {'promo_codes': PromoCode.objects.all()}
    return render(request,"promo_codes.html",context)

def promo_code_registration(request):
    if request.method =="POST":
        code = request.POST["code"]
        promo_code = PromoCode(code=code)
        promo_code.save()
        context={"promo_codes": PromoCode.objects.all()}
        return render(request, "promo_codes.html", context)
    else:
        return render(request, "promo_code_registration.html")

def delete_code(request, id):
    code=PromoCode.objects.get(id=id)
    code.delete()
    context = {'promo_codes': PromoCode.objects.all()}
    return render(request,"promo_codes.html",context)

def promo_code_update(request, id):
    
    promo_code=PromoCode.objects.get(id=id)
    if request.method=="POST":
        promo_code.code=request.POST["code"]
        promo_code.save()
        context={"promo_codes": PromoCode.objects.all()}
        return render(request, "promo_codes.html", context)
    else:
        form=PromoCode({"promo_code": promo_code.code})#acá quería que en el formulario inicial me ponga los datos del que quiero editar
        return render(request, "promo_code_update.html",{"form": form, "promo_code": promo_code} )
    
