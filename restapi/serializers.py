from rest_framework import serializers

from .models import UserDocument, Document


class UserDocumentSerializer(serializers.ModelSerializer):
   class Meta:
        model = UserDocument
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
   class Meta:
        model = Document
        fields = '__all__'