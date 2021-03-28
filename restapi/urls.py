from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.loadAllHistory),
    path('document/create',views.createHistory),
    path('document/update/<int:id>',views.updateHistory),
    path('document/get-detail/<int:id>',views.loadHistory),
    path('document/get-detail/<int:idUser>/<int:idDocument>',views.loadDetailHistory),
    path('document/delete/<int:id>', views.deleteHistory),
]