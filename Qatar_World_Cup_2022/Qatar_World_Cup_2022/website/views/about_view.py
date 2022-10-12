from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from AppQatarWC2022.article import Article
from AppQatarWC2022.models import app

@login_required
def about(request):
    article = list(Article.objects.filter(title = 'Sobre nosotros'))[0]
    print(f'{article}')
    working_context = {'working_context':app.working_context(),'article': article}
    return render(request, "about.html",working_context)
