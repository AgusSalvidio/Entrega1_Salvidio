from django.shortcuts import render
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required

from AppQatarWC2022.countries.forms import CountryRegistration
from AppQatarWC2022.countries import Country

working_context = {'working_context':app.working_context()}

@login_required
def countries(request):
    app.working_context().update_form_with(CountryRegistration())
    app.working_context().update_current_url_with('countries')
    app.working_context().update_selected_object_with(Country()) 
    return render(request,"countries.html",working_context)