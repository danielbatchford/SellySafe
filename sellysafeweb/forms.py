from django import forms

from SellySafe import settings
from .models import Report


class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs["format"] = settings.DATETIME_INPUT_FORMATS[0]
        super().__init__(**kwargs)


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ("contents", "lat", "long", "datetime")
        widgets = {'datetime': DateTimeInput()}
