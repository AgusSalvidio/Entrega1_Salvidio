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
    context = {'user_profile':UserProfile.objects.get(internal_user=request.user)}
    return render(request,"home.html",context)

@login_required
def player_stickers(request):
    context = {'player_stickers': PlayerSticker.objects.all(),'form':PlayerStickerRegistration()}
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
            response = player_stickers(request)
            return HttpResponse(response)
        else:
            response = player_stickers(request)
            return HttpResponse(response)
    else:
        context = {'form':PlayerStickerRegistration()}
        return render(request, "player_sticker_registration.html",context)

@login_required
def player_sticker_unregistration(request, id):
    player_sticker=PlayerSticker.objects.get(id=id)
    player_sticker.delete()
    response = player_stickers(request)
    return HttpResponse(response)

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
        response = player_stickers(request)
        return HttpResponse(response)
    else:
        form=PlayerStickerRegistration({'first_name':player_sticker.first_name,'last_name':player_sticker.last_name,'country':player_sticker.country,'birthdate':player_sticker.birthdate,'position':player_sticker.position})
        context = {'form':form,'player_sticker':player_sticker}
        return render(request, "player_sticker_update.html",context)

@login_required
def promo_codes(request):
    context={"promo_codes": PromoCode.objects.all(),'form':PromoCodeRegistration()}
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
            response = promo_codes(request)
            return HttpResponse(response)
        else:
            response = promo_codes(request)
            return HttpResponse(response)
    else:
        context = {"form":PromoCodeRegistration()} 
        return render(request, "promo_code_registration.html",context)
        
@login_required
def promo_code_update(request, id):
    promo_code=PromoCode.objects.get(id=id)
    if request.method=="POST":
        promo_code.code=request.POST["code"]
        promo_code.save()
        response = promo_codes(request)
        return HttpResponse(response)
    else:
        form = PromoCodeRegistration({"code": promo_code.code})
        context ={"form":form , "promo_code": promo_code} 
        return render(request, "promo_code_update.html",context)

@login_required
def promo_code_unregistration(request, id):
    code=PromoCode.objects.get(id=id)
    code.delete()
    response = promo_codes(request)
    return HttpResponse(response)

def login_request(request):
    if request.method == 'POST':
        form = SignIn(request,data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                context = {'user_profile':UserProfile.objects.get(internal_user=request.user)}
                return render (request,'home.html',context)
            else:
                return render(request,'login.html',{'form':form,'auth_message':'Usuario y/o contraseña incorrectos'})
        else:
                return render(request,'login.html',{'form':form,'auth_message':'Usuario y/o contraseña incorrectos'})
    else:
        form = SignIn()
        return render(request,'login.html',{'form':form})    

def sign_up(request):
    if request.method == 'POST':
        internal_user_form = UserRegistration(request.POST,request.FILES)
        if internal_user_form.is_valid():
            information = internal_user_form.cleaned_data
            birthdate = information['birthdate'] 
            country = information['country']
            avatar = information['avatar']
            user = internal_user_form.save()
            user_profile = UserProfile(internal_user = user, birthdate = birthdate, country = country, avatar_image = avatar)
            user_profile.save()
            context = {'form':SignIn()}
            return render(request,'login.html',context)
        else:
            context = {'form':UserRegistration(),'auth_message':f"No se pudo crear al usuario debido a {internal_user_form.errors}"}
            return render(request,'sign_up.html',context)
    else:
        context = {'form':UserRegistration()}
        return render(request,'sign_up.html',context)
