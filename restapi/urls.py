from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.loadAllHistory),
    path('create/',views.createHistory),
    path('update/',views.updateHistory),
    path('get-detail/<int:id>',views.loadHistory),
    path('get-detail/<int:idUser>/<int:idDocument>',views.loadDetailHistory),
    path('delete/<int:id>', views.deleteHistory),
]