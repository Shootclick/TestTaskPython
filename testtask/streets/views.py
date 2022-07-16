from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from streets.serializers import StreetSerializer


class StreetCreateView(CreateAPIView):
    serializer_class = StreetSerializer
