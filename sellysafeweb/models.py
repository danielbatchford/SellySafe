from django.db import models


# Create your models here.

class Report(models.Model):
    # HARR, ROBB, INDE, SUSP
    type = models.CharField(max_length=4, default="")
    contents = models.TextField(max_length=1000, default="")
    lat = models.FloatField()
    long = models.FloatField()
    date = models.DateTimeField(default="")
