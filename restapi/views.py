from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from django.core import serializers
from rest_framework.renderers import JSONRenderer

from .models import UserDocument
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserDocumentSerializer

from rest_framework import viewsets


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loadAllHistory(request):
    userdocument = UserDocument.objects.all()
    serializer = UserDocumentSerializer(userdocument, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createHistory(request):
    User_id=request.data['User_id']
    Document_id= request.data['Document_id']
    page = request.data['page']
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO RESTAPI_USERDOCUMENT(DOCUMENT_ID,USER_ID,PAGE) VALUES ("+Document_id+","+User_id+","+page+");")
    return Response("Success")


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateHistory(request):
    User_id = str(request.data['User_id'])
    Document_id = str(request.data['Document_id'])
    page = str(request.data['page'])
    with connection.cursor() as cursor:
        cursor.callproc("updateDBUSERDOCUMENT",[Document_id,User_id,page])
    return Response("Success")


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loadHistory(request, id):
    userdocument = UserDocument.objects.get(id=id)
    serializer = UserDocumentSerializer(userdocument)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loadDetailHistory(request, idUser, idDocument):
    userdocument = UserDocument.objects.get(User_id=idUser, Document_id=idDocument)
    serializer = UserDocumentSerializer(userdocument)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteHistory(request, id):
    userdocument = UserDocument.objects.get(id)
    userdocument.delete()
    return Response('Item successfully deleted')
