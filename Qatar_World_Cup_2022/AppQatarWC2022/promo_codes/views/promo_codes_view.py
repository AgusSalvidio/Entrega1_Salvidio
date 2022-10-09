from django.shortcuts import render
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required

from AppQatarWC2022.promo_codes.forms import PromoCodeRegistration
from AppQatarWC2022.promo_codes import PromoCode

working_context = {'working_context':app.working_context()}

@login_required
def promo_codes(request):
    app.working_context().update_form_with(PromoCodeRegistration())
    app.working_context().update_current_url_with('promo_codes')
    app.working_context().update_selected_object_with(PromoCode()) 
    return render(request,"promo_codes.html",working_context)