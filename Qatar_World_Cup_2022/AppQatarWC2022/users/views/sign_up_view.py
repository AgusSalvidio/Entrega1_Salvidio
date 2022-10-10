from django.shortcuts import render,redirect
from django.contrib import messages
from AppQatarWC2022.models import app

from AppQatarWC2022.users.forms import UserRegistration,SignIn
from AppQatarWC2022.users import UserProfile

working_context = {'working_context':app.working_context()}

def sign_up(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()          
            user_profile = UserProfile.from_form_using(form.cleaned_data,user)
            app.working_context().register(user_profile)
            return redirect( 'login' )
        else:
            messages.error(request,f'No se pudo crear al usuario debido a {form.errors}')
            app.working_context().update_form_with(UserRegistration())
            return redirect('sign_up')
    else:
        app.working_context().update_form_with(UserRegistration())
        return render(request,'sign_up.html',working_context)