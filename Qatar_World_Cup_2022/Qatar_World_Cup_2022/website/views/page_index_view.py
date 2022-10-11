from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from AppQatarWC2022.models import app
working_context = {'working_context':app.working_context()}

@login_required
def pages(request):
    return render(request, "page_index.html",working_context)
