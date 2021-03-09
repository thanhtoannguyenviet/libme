from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Document, Topic


# from .forms import DocumentForm


def home_page(request):
    document = Document.objects.all()
    context = {
        "document": document
    }
    return render(request, "home/home_page.html", context)


def navigation(request):
    topic = Topic.objects.all()
    context = {
        "topic": topic
    }
    return render(request, "home/navigation.html", context)


class DocumentView:

    def index(request):
        document = Document.objects.all()
        context = {
            "document": document
        }
        return render(request, "home/home_page.html", context)

    def create(request):
        form = DocumentForm(request.POST or None, request.FILES or None)
        if request.method == 'POST' and request.FILES['link']:
            if form.is_valid():
                link = request.FILES['link']
                fs = FileSystemStorage()
                filename = fs.save(link.name, link)
                form.link = filename
                form.save()
                return redirect('/')
        else:
            context = {"form": form}

        return render(request, 'document/create.html', context)

    def edit(request, id):
        document = Document.objects.get(id=id)
        form = DocumentForm(request.POST or None, request.FILES or None, instance=document)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'document/create.html', {'form': form})

    def delete(request, id):
        document = Document.objects.get(id=id)
        document.delete()

