from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions

from .models import UserDocument
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserDocumentSerializer

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loadAllHistory(request):
    userdocument = UserDocument.objects.all()

    serializer = UserDocumentSerializer(userdocument, many= True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def createHistory(request):
    serializer = UserDocumentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateHistory(request,pk):
    userDocument = UserDocument.objects.get(id=pk)
    serializer = UserDocumentSerializer(instance=userDocument,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loadHistory(request, id):
    userdocument = UserDocument.objects.get(id=id)

    serializer = UserDocumentSerializer(userdocument, many= True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loadDetailHistory(request, idUser, idDocument):
    userdocument = UserDocument.objects.get(idUser = idUser,idDocument = idDocument)

    serializer = UserDocumentSerializer(userdocument, many= True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def deleteHistory(request, id):
    userdocument = UserDocument.objects.get(id)
    userdocument.delete()
    return Response('Item successfully deleted')
