from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from djangoProject import settings
# from documentsite.views import home_page, create, edit, index, navigation
from documentsite import views,urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('document/', include(urls)),
    # path('document/create', create),
    # path('document/edit', edit),
    # path('document/index', index),
    path('navigation', views.navigation, name='navigation'),
    # path('treenav/', include('treenav.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)