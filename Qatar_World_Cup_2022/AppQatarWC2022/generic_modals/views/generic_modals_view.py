from django.shortcuts import render,redirect
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import sys

#Because its generic, when the objects is initializated, needs to know the real class, so needs to be imported
from AppQatarWC2022.promo_codes import PromoCode
from AppQatarWC2022.promo_codes.forms import PromoCodeRegistration

from AppQatarWC2022.stickers import PlayerSticker
from AppQatarWC2022.stickers.forms import PlayerStickerRegistration

working_context = {'working_context':app.working_context()}

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