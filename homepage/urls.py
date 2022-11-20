from django.urls import path

from homepage import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('registration', views.registration, name='registration'),
]
