import json

import cx_Oracle
from django.db import connection
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions
from django.core import serializers
from rest_framework.renderers import JSONRenderer

from .models import UserDocument, Document
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import UserDocumentSerializer,DocumentSerializer

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
    User_id = request.data['User_id']
    Document_id = request.data['Document_id']
    page = request.data['page']
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO RESTAPI_USERDOCUMENT(DOCUMENT_ID,USER_ID,PAGE) VALUES (" + Document_id + "," + User_id + "," + page + ");")
    return Response("Success")


@api_view(['PUT'])
@permission_classes((permissions.AllowAny,))
def updateHistory(request):
    User_id = str(request.data['User_id'])
    Document_id = str(request.data['Document_id'])
    page = str(request.data['page'])
    with connection.cursor() as cursor:
        cursor.callproc("updateDBUSERDOCUMENT", [Document_id, User_id, page])
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


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def loadDocument(request, id, pageNumber, pageSize):
    with connection.cursor() as cursor:
        # refCursorVar = cursor.var(Cursor)
        # cursor.callproc("LOADDOCUMENT", [str(id), str(pageNumber), str(pageSize),refCursorVar])
        # cursor.callproc("LOADDOCUMENT", [id, pageNumber, pageSize,refCursorVar])
        cursor.execute("""
           declare
            cust_cur sys_refcursor;
            
              begin
          LOADDOCUMENT("""+str(id)+","+str(pageNumber)+","+str(pageSize)+""", cust_cur);
            dbms_sql.return_result(cust_cur);

        end;        
        """)
        list = []
        for implicitCursor in cursor.getimplicitresults():
            for row in implicitCursor:
                document = Document(id=row[0], title=row[1], description=row[2], is_active=row[3], createDate=row[4],
                                    editDate=row[5], link=row[6], image=row[7], type=row[8])
                list.append(document)
        serializer = DocumentSerializer(list, many=True)
    return Response(serializer.data)
