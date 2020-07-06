from django.db import models
from django.utils import timezone


# Create your models here.

class Report(models.Model):
    contents = models.TextField(max_length=200, default="")
    lat = models.FloatField()
    long = models.FloatField()
    datetime = models.DateTimeField(default=timezone.now)