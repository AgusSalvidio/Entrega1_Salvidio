from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from AppQatarWC2022.article import Article

@login_required
def about(request):
    article = list(Article.objects.filter(title = 'Sobre nosotros'))[0]
    print(f'{article}')
    context = {'article': article}
    return render(request, "about.html",context)
