from django.shortcuts import render
from AppQatarWC2022.models import app
from django.contrib.auth.decorators import login_required

from AppQatarWC2022.stickers.forms import PlayerStickerRegistration
from AppQatarWC2022.stickers import PlayerSticker

working_context = {'working_context':app.working_context()}

@login_required
def player_stickers(request):
    app.working_context().update_form_with(PlayerStickerRegistration())
    app.working_context().update_current_url_with('player_stickers')
    app.working_context().update_selected_object_with(PlayerSticker()) 
    return render(request,"player_stickers.html",working_context)