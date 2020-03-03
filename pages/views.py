from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    ctx = {}
    return render(request, "index.html", ctx)


def login_view(request, *args, **kwargs):
    ctx = {}
    return render(request, "login.html", ctx)
