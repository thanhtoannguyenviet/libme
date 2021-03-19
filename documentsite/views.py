from django.shortcuts import render, redirect
from django.views.generic import DetailView, TemplateView
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

from .decorators import unauthenticated_user, allowed_users, admin_only
from .forms import DocumentForm, TopicForm, TopicDocumentForm, CreateUserForm
from .models import Document, Topic, TopicDocument
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required


# from .forms import DocumentForm

@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            username = form.cleaned_data.get('email')
            messages.success(request, 'Account was created for' + username)
    context = {'form': form}
    return render(request, 'registration/signin.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            redirect('/')
        else:
            messages.info(request, 'User or password is incorrect')
    context = {}
    return render(request, 'registration/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


def home_page(request):
    document = Document.objects.all()
    context = {
        "document": document
    }
    return render(request, "home/home_page.html", context)


def detailPDF_page(request, id):
    document = Document.objects.get(id=id)
    context = {
        "document": document
    }
    return render(request, "home/detailPDF_page.html", context)


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

    @login_required(login_url='login')
    @admin_only
    def create(request):
        form = DocumentForm(request.POST or None, request.FILES or None)
        if request.method == 'POST' and request.FILES['link']:
            if form.is_valid():
                # link = request.FILES['link']
                # fs = FileSystemStorage()
                # filename = fs.save(link.name, link)
                # form.link = filename
                form.save()
                return redirect('/')
        else:
            context = {"form": form}

        return render(request, 'document/create.html', context)

    # @allowed_users(allowed_role=['admin'])
    @login_required(login_url='login')
    @admin_only
    def edit(request, id):
        document = Document.objects.get(id=id)
        form = DocumentForm(request.POST or None, request.FILES or None, instance=document)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'document/create.html', {'form': form})

    @login_required(login_url='login')
    @admin_only
    def delete(request, id):
        document = Document.objects.get(id=id)
        document.delete()

    def retrievefilter(request, id):
        lstopicdocument = TopicDocument.objects.filter(idTopic=id)
        if lstopicdocument is not None:
            listDocument = []
            for topicDocument in lstopicdocument:
                idDoc = topicDocument.idDocument
                if idDoc != None:
                    document = Document.objects.get(id=idDoc.id)
                    listDocument.append(document)
            return render(request, 'home/home_page.html', {'document': listDocument})


class TopicView:

    def index(request):
        topic = Topic.objects.all()
        context = {
            "topic": topic
        }
        return render(request, "home/home_page.html", context)

    @login_required(login_url='login')
    @admin_only
    def create(request):
        form = TopicForm(request.POST or None, request.FILES or None)
        if request.method == 'POST' and request.FILES['image']:
            if form.is_valid():
                link = request.FILES['image']
                fs = FileSystemStorage()
                filename = fs.save(link.name, link)
                form.link = filename
                form.save()
                return redirect('/')
        else:
            context = {"form": form}

        return render(request, 'topics/create.html', context)

    @login_required(login_url='login')
    @admin_only
    def edit(request, id):
        topic = Topic.objects.get(id=id)
        form = TopicForm(request.POST or None, request.FILES or None, instance=topic)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'topics/create.html', {'form': form})

    @login_required(login_url='login')
    @admin_only
    def delete(request, id):
        topic = Topic.objects.get(id=id)
        topic.delete()


class TopicDocumentView:

    # def index(request):
    #     topicDocument = TopicDocument.objects.all()
    #     context = {
    #         "topicDocument": topicDocument
    #     }
    #     return render(request, "home/home_page.html", context)

    @login_required(login_url='login')
    @admin_only
    def create(request):
        form = TopicDocumentForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            context = {"form": form}
        return render(request, 'document/create.html', context)

    @login_required(login_url='login')
    @admin_only
    def edit(request, id):
        topicDocument = TopicDocument.objects.get(id=id)
        form = TopicDocumentForm(request.POST or None, request.FILES or None, instance=topicDocument)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, 'document/create.html', {'form': form})

    @login_required(login_url='login')
    @admin_only
    def delete(request, id):
        topicDocument = TopicDocument.objects.get(id=id)
        topicDocument.delete()
