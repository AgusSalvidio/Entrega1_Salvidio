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
def player_cards(request):
    context = {'player_cards': PlayerCard.objects.all()}
    return render(request,"player_cards.html",context)

@login_required
def player_card_registration(request):
    if request.method =="POST":
        form = PlayerCardRegistration(request.POST)
        if form.is_valid():
            information = form.cleaned_data
            first_name = information["first_name"]
            last_name = information["last_name"]
            country = information["country"]
            birthdate = information["birthdate"]
            position = information["position"]
            player_card = PlayerCard(first_name = first_name,last_name = last_name,birthdate = birthdate,country = country,position=position)
            player_card.save()
            context={"player_cards": PlayerCard.objects.all()}
            return render(request, "player_cards.html", context)
    else:
        form = PlayerCardRegistration()
        return render(request, "player_card_registration.html",{'form':form})

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
        form = UserRegistration(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            return render(request,'AppCoder/home.html',{'auth_message':f"Usuario {username} creado correctamente"})
        else:
            return render(request,'AppCoder/user_registration.html',{'auth_message':f"No se pudo crear al usuario"})
    else:
        form = UserRegistration()
        return render(request,'AppCoder/user_registration.html',{'form':form})