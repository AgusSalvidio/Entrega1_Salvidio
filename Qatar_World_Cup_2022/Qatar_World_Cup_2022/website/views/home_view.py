from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from AppQatarWC2022.models import app

working_context = {'working_context':app.working_context()}

@login_required
def home(request):
    return render(request,"home.html",working_context)
