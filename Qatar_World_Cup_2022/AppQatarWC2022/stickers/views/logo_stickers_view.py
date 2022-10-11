from django.shortcuts import render
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required

from AppQatarWC2022.stickers.forms import LogoStickerRegistration
from AppQatarWC2022.stickers import LogoSticker

working_context = {'working_context':app.working_context()}

@login_required
def logo_stickers(request):
    app.working_context().update_form_with(LogoStickerRegistration())
    app.working_context().update_current_url_with('logo_stickers')
    app.working_context().update_selected_object_with(LogoSticker()) 
    return render(request,"logo_stickers.html",working_context)