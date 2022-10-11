from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def page_index(request):
    return render(request, "page_index.html")
