from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('catalog/', include('catalog.urls'), name='catalog'),
    path('about/', include('about.urls'), name='about'),
    path('grappelli/', include('grappelli.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('admin/', admin.site.urls, name='admin')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
