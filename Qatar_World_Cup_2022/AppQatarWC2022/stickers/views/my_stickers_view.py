from django.shortcuts import render
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required

working_context = {'working_context':app.working_context()}

@login_required
def my_stickers(request):
    return render(request,"my_stickers.html",working_context)