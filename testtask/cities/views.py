from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework import status

from cities.serializers import CitySerializer, CityStreetSerializer
from cities.models import City
from streets.models import Street


class CityCreateView(CreateAPIView):
    serializer_class = CitySerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response(response.data['id'], status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CityListView(ListAPIView):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CityStreetListView(ListAPIView):
    serializer_class = CityStreetSerializer
    # queryset = Street.objects.all()

    def get_queryset(self):
        city_id = self.kwargs['city_id']

        queryset = Street.objects.filter(city=city_id)

        return queryset

    def get(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
