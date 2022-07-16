from django.contrib import admin
from django.urls import include, path

from cities.views import CityCreateView, CityListView, CityStreetListView

app_name = 'city'
urlpatterns = [
    path('create/', CityCreateView.as_view()),
    path('', CityListView.as_view()),
    path('<uuid:city_id>/street', CityStreetListView.as_view())
]
