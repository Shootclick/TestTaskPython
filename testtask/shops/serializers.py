from rest_framework import serializers

from shops.models import Shop
from cities.models import City


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopListSerializer(serializers.ModelSerializer):
    city_name = serializers.CharField(source='city.name', read_only=True)
    street_name = serializers.CharField(source='street.name', read_only=True)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'city_name', 'street_name',
                  'house', 'timeopen', 'timeclose')
