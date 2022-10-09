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

import sys

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
    app.working_context().update_current_url_with('player_stickers')
    app.working_context().update_selected_object_with(PlayerSticker()) 
    return render(request,"player_stickers.html",working_context)

@login_required
def promo_codes(request):
    app.working_context().update_form_with(PromoCodeRegistration())
    app.working_context().update_current_url_with('promo_codes')
    app.working_context().update_selected_object_with(PromoCode()) 
    return render(request,"promo_codes.html",working_context)

@login_required
def element_registration(request,object_class_name,form_class_name):
    object_class = getattr(sys.modules[__name__], object_class_name)
    form_class= getattr(sys.modules[__name__], form_class_name)
    if request.method =="POST":
        form = form_class(request.POST)
        if form.is_valid():
            object = object_class.from_form(form.cleaned_data)
            app.working_context().register(object)
            return redirect(app.working_context().current_url())
        else:
            messages.error(request,form.errors)
            return redirect(app.working_context().current_url())
    else:
        app.working_context().update_form_with(form_class())
        return render(request, "registration_modal.html",working_context)

@login_required
def element_unregistration(request, id, object_class_name, form_class_name):
    form_class = getattr(sys.modules[__name__], form_class_name)
    object = app.working_context().identified_as(id,object_class_name)
    if request.method=="POST":
        app.working_context().unregister(object)
        return redirect(app.working_context().current_url())
    else:
        app.working_context().update_form_with(form_class())
        app.working_context().update_selected_object_with(object)
        return render(request, "unregistration_modal.html",working_context)

@login_required
def element_update(request, id, object_class_name, form_class_name):
    object_class = getattr(sys.modules[__name__], object_class_name)
    form_class = getattr(sys.modules[__name__], form_class_name)
    object = app.working_context().identified_as(id,object_class_name)
    if request.method=="POST":
        form = form_class(request.POST)
        if form.is_valid():
            updated_object = object_class.from_form(form.cleaned_data)
            app.working_context().update_with(object,updated_object)
            return redirect(app.working_context().current_url())
        else:
            messages.error(request,form.errors)
            return redirect(app.working_context().current_url())
    else:
        form_attributes = app.working_context().attributes_for(object)
        app.working_context().update_form_with(form_class(form_attributes))
        app.working_context().update_selected_object_with(object)
        return render(request, "update_modal.html",working_context)

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
