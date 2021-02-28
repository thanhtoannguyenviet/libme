from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homepage_view(*args, **kwargs):
    return HttpResponse("<H1>Hello world</H1>")
