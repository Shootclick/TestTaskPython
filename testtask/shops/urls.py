from django.contrib import admin
from django.urls import include, path, re_path
from shops.views import ShopListView, ShopCreateView


app_name = 'shop'
urlpatterns = [
    path('list', ShopListView.as_view()),
    path('create', ShopCreateView.as_view()),
]
