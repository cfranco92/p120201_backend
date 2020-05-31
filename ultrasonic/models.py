from django.db import models
import uuid

# Create your models here.

class Ultrasonic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField(verbose_name='Tipo', max_length=20)
    value = models.IntegerField(verbose_name='Valor')
    placeLatitude = models.FloatField(verbose_name='LatitudLugar')
    placeLength = models.FloatField(verbose_name='PlaceLength')
    landArea = models.TextField(verbose_name='LandArea')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)