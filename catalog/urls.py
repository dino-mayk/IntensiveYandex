from django.urls import path, re_path

from catalog import views

app_name = 'catalog'

urlpatterns = [
    path('', views.Item_list.as_view(), name='item_list'),
    re_path(
        r'^(?P<pk>[1-9]\d*)/$',
        views.Item_detail.as_view(),
        name='item_detail'),
]
