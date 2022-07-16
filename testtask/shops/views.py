from datetime import datetime
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from shops.serializers import ShopSerializer, ShopListSerializer
from shops.models import Shop


class ShopCreateView(CreateAPIView):
    serializer_class = ShopSerializer

    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            return Response(response.data['id'], status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class ShopListView(ListAPIView):
    serializer_class = ShopListSerializer

    def get_queryset(self):
        queryset = Shop.objects.all()
        city = self.request.query_params.get('city')

        current_hour = datetime.now().hour
        street = self.request.query_params.get('street')
        open = self.request.query_params.get('open')

        if city:
            queryset = queryset.filter(city__name=city)
        if street:
            queryset = queryset.filter(street__name=street)
        if open:
            if int(open) == 1:
                queryset = queryset.filter(
                    timeopen__lte=current_hour, timeclose__gte=current_hour)
            elif int(open) == 0:
                queryset = queryset.filter(
                    timeopen__gte=current_hour, timeclose__lte=current_hour)

        return queryset

    def get(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            return Response(response.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
