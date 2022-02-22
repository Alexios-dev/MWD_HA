from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Ansicht in SiteView/Views.py")
# Create your views here.

