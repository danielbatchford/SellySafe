from django import forms
import datetime
from SellySafe import settings
from .models import Report


class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs["format"] = settings.DATETIME_INPUT_FORMATS[0]
        #kwargs["min"] = datetime.datetime.now().strftime(settings.DATETIME_INPUT_FORMATS[0])
        super().__init__(**kwargs)


class ReportForm(forms.ModelForm):
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
