from rest_framework import serializers

from cities.models import City
from streets.models import Street


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CityStreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('name',)
