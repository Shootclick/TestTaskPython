import uuid
from django.db import models

from cities.models import City
from streets.models import Street


class Shop(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
    street = models.ForeignKey(Street, on_delete=models.PROTECT)
    house = models.CharField(max_length=10)
    timeopen = models.IntegerField()
    timeclose = models.IntegerField()
