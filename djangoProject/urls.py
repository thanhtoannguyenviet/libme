from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from djangoProject import settings
# from documentsite.views import home_page, create, edit, index, navigation
from documentsite import views,urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),
    path('navigation', views.navigation, name='navigation'),
    path('detailpage/<id>', views.detailPDF_page),
    # path('detailpage/<id>', views.PDFUserDetailView.as_view),
    path('', views.home_page),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)