
from django.urls import path
from documentsite import views

urlpatterns = [
    path('create', views.DocumentView.create),
    path('edit/<id>', views.DocumentView.edit),
    path('index', views.DocumentView.index),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)