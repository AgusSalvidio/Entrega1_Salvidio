from django.shortcuts import redirect, render
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required

working_context = {'working_context':app.working_context()}

@login_required
def my_album(request):
    if request.method =="POST":
        pass
    else:
        app.working_context().refresh_album()
        return render(request,"my_album.html",working_context)

@login_required
def qualified_countries(request):
    if request.method =="POST":
        pass
    else:
        return render(request,"countries_modal.html",working_context)

@login_required
def update_current_album_page(request,country_name):
    if request.method =="POST":
        pass
    else:
        app.working_context().refresh_album()
        selected_page = app.working_context().page_for(country_name)
        app.working_context().update_current_album_page_with(selected_page)
        return render(request,"my_album.html",working_context)

@login_required
def next_page(request):
    if request.method =="POST":
        pass
    else:
        next_page = app.working_context().next_page()
        app.working_context().update_current_album_page_with(next_page)
        return render(request,"my_album.html",working_context)

@login_required
def previous_page(request):
    if request.method =="POST":
        pass
    else:
        previous_page = app.working_context().previous_page()
        app.working_context().update_current_album_page_with(previous_page)
        return render(request,"my_album.html",working_context)

@login_required
def glue_sticker(request,id):
    if request.method =="POST":
        pass
    else:
        generated_sticker = app.working_context().generated_sticker_of(id)
        country_name = generated_sticker.country().full_name()
        generated_sticker.glue_sticker()
        app.working_context().refresh_album()
        selected_page = app.working_context().page_for(country_name)
        app.working_context().update_current_album_page_with(selected_page)
        return render(request,"my_album.html",working_context)
   
