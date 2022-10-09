from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from AppQatarWC2022.models import app

from AppQatarWC2022.users.forms import SignIn

working_context = {'working_context':app.working_context()}

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