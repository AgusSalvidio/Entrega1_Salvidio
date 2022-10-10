from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib import messages
from AppQatarWC2022.models import app

from AppQatarWC2022.users.forms import UserRegistration,UserProfileUpdate
from AppQatarWC2022.users.user_profile import UserProfile

working_context = {'working_context':app.working_context()}

def update_user_with_data_from(user,form_data):
    user.first_name = form_data.get('first_name')
    user.last_name = form_data.get('last_name')
    user.email = form_data.get('email')
    user.save()

def update_user_profile(request):
    user_profile = app.working_context().logged_user()
    user = request.user
    if request.method == 'POST':
        form = UserProfileUpdate(request.POST,request.FILES)
        if form.is_valid():
            form_data = form.cleaned_data
            update_user_with_data_from(user,form_data)
            updated_user_profile = UserProfile.from_form_using(form.cleaned_data,user)
            app.working_context().update_with(user_profile,updated_user_profile)
            messages.success(request,'El perfil se actualizó satisfactoriamente')
            return redirect('update_user_profile')
        else:
            messages.error(request,form.errors)
            return redirect('update_user_profile')
    else:
        app.working_context().update_form_with(
            UserProfileUpdate(initial={
                'first_name' : user_profile.first_name(), 
                'last_name' : user_profile.last_name(), 
                'birthdate' : user_profile.birth_date(), 
                'email' :  user_profile.email(), 
                'country' : user_profile.nationality(), 
                'username': user_profile.username(), 
                'avatar' : user_profile.avatar()}))
        app.working_context().update_selected_object_with(user_profile)
        return render(request,'update_user_profile.html',working_context)   