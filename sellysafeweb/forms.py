from django import forms
import datetime

from django.core.exceptions import ValidationError

from SellySafe import settings
from .models import Report


class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs["format"] = settings.DATETIME_INPUT_FORMATS[0]
        super().__init__(**kwargs)


class ReportForm(forms.ModelForm):

    def clean(self):
        cd = self.cleaned_data

        if cd['datetime'] < datetime.datetime.now() - datetime.timedelta(days = settings.SHOW_DURATION):
            raise ValidationError("Please add reports in the last {} days".format(settings.SHOW_DURATION))
        if cd['datetime'] > datetime.datetime.now():
            raise ValidationError("Report time cannot be in the future.")

        bounds = settings.BOUNDS
        bl = bounds[0]
        tr = bounds[1]
        if cd['long'] > tr[0] or cd['long'] < bl[0]:
            raise ValidationError("Longitude out of bounds")
        if cd['lat'] > tr[1] or cd['lat'] < bl[1]:
            raise ValidationError("Latitude out of bounds")

    class Meta:
        model = Report
        fields = ("contents", "lat", "long", "datetime")
        widgets = {'datetime': DateTimeInput(),
                   'lat': forms.HiddenInput(),
                   'long': forms.HiddenInput()}

        labels = {
            'contents': 'Please describe what happened',
            'datetime': 'When did this happen?'
        }
