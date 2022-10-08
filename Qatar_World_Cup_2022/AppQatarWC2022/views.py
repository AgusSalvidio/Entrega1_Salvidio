from django.shortcuts import render,redirect
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

from AppQatarWC2022.models import app

from django.contrib import messages
from assertions import InstanceCreationFailed, SystemRestrictionInfringed

working_context = {'working_context':app.working_context()}

@login_required
def home(request):
    return render(request,"home.html",working_context)

@login_required
def my_album(request):
    if request.method =="POST":
        pass
    else:
        app.working_context().refresh_album()
        return render(request,"my_album.html",working_context)

@login_required
def player_stickers(request):
    app.working_context().update_form_with(PlayerStickerRegistration())
    return render(request,"player_stickers.html",working_context)

@login_required
def player_sticker_registration(request):
    if request.method =="POST":
        form = PlayerStickerRegistration(request.POST,request.FILES)
        if form.is_valid():
            player_sticker = PlayerSticker.from_form(form.cleaned_data)
            app.working_context().register_player_sticker(player_sticker)
            return redirect('player_stickers')
        else:
            messages.error(request,form.errors)
            return redirect('player_stickers')
    else:
        app.working_context().update_form_with(PlayerStickerRegistration())
        return render(request, "player_sticker_registration.html",working_context)

@login_required
def player_sticker_unregistration(request, id):
    player_sticker= app.working_context().player_sticker_identified_as(id)
    if request.method=="POST":
        app.working_context().unregister_player_sticker(player_sticker)
        return redirect('player_stickers')
    else:
        form = PlayerStickerRegistration({'first_name':player_sticker.first_name,'last_name':player_sticker.last_name,'country':player_sticker.country,'birthdate':player_sticker.birthdate,'position':player_sticker.position,'sticker_image':player_sticker.sticker_image,'rarity_category': player_sticker.rarity_category,'slot':player_sticker.slot})
        app.working_context().update_form_with(form)
        app.working_context().update_selected_object_with(player_sticker)
        return render(request, "player_sticker_unregistration.html",working_context)

@login_required
def player_sticker_update(request, id):
    player_sticker = app.working_context().player_sticker_identified_as(id)
    if request.method=="POST":
        form = PlayerStickerRegistration(request.POST,request.FILES)
        if form.is_valid():
            updated_player_sticker = PlayerSticker.from_form(form.cleaned_data)
            app.working_context().update_player_sticker_with(player_sticker,updated_player_sticker)
            return redirect('player_stickers')
        else:
            messages.error(request,form.errors)
            return redirect('player_stickers')
    else:
        form = PlayerStickerRegistration({'first_name':player_sticker.first_name,'last_name':player_sticker.last_name,'country':player_sticker.country,'birthdate':player_sticker.birthdate,'position':player_sticker.position,'sticker_image':'/media/stickers/angel-dimaria.jpg','rarity_category': player_sticker.rarity_category,'slot':player_sticker.slot})
        app.working_context().update_form_with(form)
        app.working_context().update_selected_object_with(player_sticker)
        return render(request, "player_sticker_update.html",working_context)

@login_required
def promo_codes(request):
    app.working_context().update_form_with(PromoCodeRegistration())
    return render(request,"promo_codes.html",working_context)

@login_required
def promo_code_registration(request):
    if request.method =="POST":
        form = PromoCodeRegistration(request.POST)
        if form.is_valid():
            promo_code = PromoCode.from_form(form.cleaned_data)
            app.working_context().register_promo_code(promo_code)
            return redirect('promo_codes')
        else:
            messages.error(request,form.errors)
            return redirect('promo_codes')
    else:
        app.working_context().update_form_with(PromoCodeRegistration())
        return render(request, "promo_code_registration.html",working_context)
        
@login_required
def promo_code_update(request, id):
    promo_code = app.working_context().promo_code_identified_as(id)
    if request.method=="POST":
        form = PromoCodeRegistration(request.POST)
        if form.is_valid():
            updated_promo_code = PromoCode.from_form(form.cleaned_data)
            app.working_context().update_promo_code_with(promo_code,updated_promo_code)
            return redirect('promo_codes')
        else:
            messages.error(request,form.errors)
            return redirect('promo_codes')
    else:
        app.working_context().update_form_with(PromoCodeRegistration({"code": promo_code.code}))
        app.working_context().update_selected_object_with(promo_code)  
        return render(request, "promo_code_update.html",working_context)

@login_required
def promo_code_unregistration(request, id):
    promo_code = app.working_context().promo_code_identified_as(id)
    if request.method=="POST":
        app.working_context().unregister_promo_code(promo_code)
        return redirect('promo_codes')
    else:
        app.working_context().update_form_with(PromoCodeRegistration({"code": promo_code.code}))
        app.working_context().update_selected_object_with(promo_code)   
        return render(request, "promo_code_unregistration.html",working_context)

def login_request(request):
    if request.method == 'POST':
        form = SignIn(request,data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                app.working_context().store_logged_user(request.user)
                return render (request,'home.html',working_context)
            else:
                app.working_context().update_form_with(form)
                messages.error(request,'Usuario y/o contraseña incorrectos')
                return redirect('login')
        else:
                app.working_context().update_form_with(form)
                messages.error(request,'Usuario y/o contraseña incorrectos')
                return redirect('login')
    else:
        app.working_context().update_form_with(SignIn())
        return render(request,'login.html',working_context)    

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
            app.working_context().update_form_with(SignIn())
            return render(request,'login.html',working_context)
        else:
            app.working_context().update_form_with(UserRegistration())
            messages.error(request,f'No se pudo crear al usuario debido a {internal_user_form.errors}')
            return redirect('sign_up')
    else:
        app.working_context().update_form_with(UserRegistration())
        return render(request,'sign_up.html',working_context)
