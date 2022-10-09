from django.shortcuts import render,redirect
from django.contrib import messages
from AppQatarWC2022.models import app

from AppQatarWC2022.users.forms import UserRegistration,SignIn
from AppQatarWC2022.users import UserProfile

working_context = {'working_context':app.working_context()}

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