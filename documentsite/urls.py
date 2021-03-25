
from django.urls import path
from documentsite.views import DocumentView, TopicView, TopicDocumentView

urlpatterns = [
    path('document/create', DocumentView.create),
    path('document/edit/<id>', DocumentView.edit),
    path('document/index', DocumentView.index),
    path('document/detail/<id>', DocumentView.detail),
    path('topic/create', TopicView.create),
    path('topic/index', TopicView.index),
    path('topic/edit/<id>', TopicView.edit),
    path('topic/detail/<id>', TopicView.detail),
    path('topic/<id>', DocumentView.retrievefilter),
    path('topicdocument/create', TopicDocumentView.create),
    path('topicdocument/edit/<id>', TopicDocumentView.edit),

]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)