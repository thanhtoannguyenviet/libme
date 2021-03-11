
from django.urls import path
from documentsite.views import DocumentView, TopicView

urlpatterns = [
    path('document/create', DocumentView.create),
    path('document/edit/<id>', DocumentView.edit),
    path('document/index', DocumentView.index),
    path('topic/create', TopicView.create),
    path('topic/edit/<id>', TopicView.edit),
    path('topic/index', TopicView.index),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)