from django.urls import include, path


urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('catalog/', include('catalog.urls'), name='catalog'),
    path('', include('catalog.urls'), name='catalogItem'),
    path('about/', include('about.urls'), name='about'),
]
