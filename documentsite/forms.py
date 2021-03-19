from django import forms
from django.db import models
from .models import Document, Topic, TopicDocument, User

class CreateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','phonenumber','fullname','avatar','dob','password']


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'description', 'link', 'type', 'image']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title', 'description', 'image']


class TopicDocumentForm(forms.ModelForm):
    class Meta:
        model = TopicDocument
        fields = '__all__'