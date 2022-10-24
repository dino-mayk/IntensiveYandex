from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.item_list),
    path('catalog/<int:pk>/', views.item_detail)
]
