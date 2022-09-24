from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.urls import reverse_lazy

from AppQatarWC2022.forms import *

from django.contrib.auth.forms import AuthenticationForm

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate

from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request,"home.html")
@login_required
def users(request):
    context = {'users': User.objects.all()}
    return render(request,"users.html",context)

def user_registration(request):
    if request.method == 'POST':
        #revisar que trae el formulario de UserRegistration
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
@login_required
def filtered_users(request):
    if request.GET["first_name"]:
        user_name = request.GET["first_name"]
        users = User.objects.filter(first_name=user_name)
        return render(request,"filtered_users.html",{"users":users})
    else:
        return render(request,"users.html")

@login_required
def user_delete(request, id):
    user=User.objects.get(id=id)
    user.delete()
    context={"user":User.objects.all()}
    return render (request, "users.html", context)

@login_required
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

def player_stickers(request):
    context = {'player_stickers': PlayerSticker.objects.all()}
    return render(request,"player_stickers.html",context)

@login_required
def player_sticker_registration(request):
    if request.method =="POST":
        form = PlayerStickerRegistration(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            first_name = information["first_name"]
            last_name = information["last_name"]
            country = information["country"]
            birthdate = information["birthdate"]
            position = information["position"]
            player_card = PlayerSticker(first_name = first_name,last_name = last_name,birthdate = birthdate,country = country,position=position)
            player_card.save()
            context={"player_stickers": PlayerSticker.objects.all()}
            return render(request, "player_stickers.html", context)
    else:
        form = PlayerStickerRegistration()
        return render(request, "player_sticker_registration.html",{'form':form})

@login_required
def player_sticker_delete(request, id):
    player_sticker=PlayerSticker.objects.get(id=id)
    player_sticker.delete()
    context={"player_stickers":PlayerSticker.objects.all()}
    return render (request, "player_stickers.html", context)

@login_required
def player_sticker_update(request, id):
    player_sticker=PlayerSticker.objects.get(id=id)
    if request.method=="POST":
        player_sticker.first_name = request.POST["first_name"]
        player_sticker.last_name = request.POST["last_name"]
        player_sticker.country = request.POST["country"]
        player_sticker.birthdate = request.POST["birthdate"]
        player_sticker.position = request.POST["position"]
        player_sticker.save()
        context={"player_stickers": PlayerSticker.objects.all()}
        return render(request, "player_stickers.html", context)
    else:
        form=PlayerSticker()
        return render(request, "player_sticker_update.html",{"form": form, "player_sticker":player_sticker} )

@login_required
def promo_codes(request):
    context = {'promo_codes': PromoCode.objects.all()}
    return render(request,"promo_codes.html",context)

@login_required
def promo_code_registration(request):
    if request.method =="POST":
        form = PromoCodeRegistration(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            code = information["code"]
            promo_code = PromoCode(code=code)
            promo_code.save()
            context={"promo_codes": PromoCode.objects.all()}
            return render(request, "promo_codes.html", context)
    else:
        form = PromoCodeRegistration()
        return render(request, "promo_code_registration.html",{'form':form})

@login_required
def delete_code(request, id):
    code=PromoCode.objects.get(id=id)
    code.delete()
    context = {'promo_codes': PromoCode.objects.all()}
    return render(request,"promo_codes.html",context)

@login_required
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

def login_request(request):
    if request.method == 'POST':
        form = SignIn(request,data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return render (request,'home.html',{'user':user})
            else:
                return render(request,'login.html',{'form':form,'auth_message':'Usuario y/o contraseña incorrectos'})
        else:
                return render(request,'login.html',{'form':form,'auth_message':'Usuario y/o contraseña incorrectos'})
    else:
        form = SignIn()
        return render(request,'login.html',{'form':form})    

def sign_up(request):
    if request.method == 'POST':
        internal_user = UserRegistration(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            birthdate = information['birthdate'] 
            country = information['country']
            username = information['username']
            avatar = information['avatar']
            internal_user.save()
            user_profile = UserProfile(internal_user = internal_user, birthdate = birthdate, country = country, avatar = avatar, basura_intergalactica = 'algo')
            user_profile.save()
            return render(request,'login.html')
        else:
            return render(request,'sign_up.html',{'auth_message':f"No se pudo crear al usuario"})
    else:
        form = UserRegistration()
        return render(request,'sign_up.html',{'form':form})
