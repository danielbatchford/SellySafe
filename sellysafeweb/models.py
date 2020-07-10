from django.db import models
from django.utils import timezone

# Model to hold report location, contents and datetime
class Report(models.Model):
    contents = models.TextField(max_length=200, default="")
    lat = models.FloatField()
    long = models.FloatField()
    datetime = models.DateTimeField(default=timezone.now)


# Model to hold app feedback
class Feedback(models.Model):
    contents = models.TextField(max_length=1000, default="")
    email = models.CharField(max_length=50)
