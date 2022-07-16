from django.contrib import admin
from django.urls import include, path
from streets.views import StreetCreateView


app_name = 'street'
urlpatterns = [
    path('', StreetCreateView.as_view())
]
