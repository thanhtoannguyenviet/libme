from django.shortcuts import render
from django.http import HttpResponse
from .models import Document, Topic


def home_page(request):
    document = Document.objects.all()
    context = {
        "document": document
    }
    return render(request, "home/home_page.html", context)


# def navigation(request):
#     topic = Topic.objects.all()
#     context = {
#         "topic": topic
#     }
#     return render(request,"home/navigation.html",context)
