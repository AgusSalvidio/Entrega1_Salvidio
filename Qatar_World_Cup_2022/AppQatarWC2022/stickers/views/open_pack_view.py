from django.shortcuts import render
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required

working_context = {'working_context':app.working_context()}

@login_required
def open_pack(request):
    sticker_pack = app.working_context().sticker_pack_for(app.working_context().logged_user())
    return render(request,"open_pack.html",{'sticker_pack':sticker_pack,'working_context':app.working_context()}) 