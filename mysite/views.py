from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required


@login_required
def home_page(request):

    context = "hello???"
    return render(request, "home.html", {'context': context})
