import datetime

from django.db import models


# Create your models here.

class Report(models.Model):
    contents = models.TextField(max_length=1000, default="")
    lat = models.FloatField()
    long = models.FloatField()
    datetime = models.DateTimeField(default=datetime.datetime.now())
