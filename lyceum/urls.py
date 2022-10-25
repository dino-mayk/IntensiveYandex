from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('catalog/', include('catalog.urls'), name='catalog'),
    path('about/', include('about.urls'), name='about'),
    path('admin/', admin.site.urls, name='admin')
]
