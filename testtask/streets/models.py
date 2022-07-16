import uuid
from django.db import models

from cities.models import City


class Street (models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.PROTECT)
