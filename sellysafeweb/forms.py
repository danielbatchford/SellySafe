from captcha.widgets import ReCaptchaV2Checkbox, ReCaptchaV3
from django import forms
from django.core.exceptions import ValidationError
from captcha.fields import ReCaptchaField
from SellySafe import settings
from .models import Report


class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        kwargs["format"] = settings.DATETIME_INPUT_FORMATS[0]
        super().__init__(**kwargs)


class ReportForm(forms.Form):
    CHOICES = [(0, 'Just now'),
               (5, '5 minutes ago'),
               (15, '15 minutes ago'),
               (30, '30 minutes ago'),
               (1, '1 hour ago'),
               (2, '2 hours ago'),
               (3, '3 hours ago'),
               (4, '4 hours ago')]
    datetime = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="When did this happen?",
                                 required=True, initial = 0)
    lat = forms.FloatField(widget=forms.HiddenInput)
    long = forms.FloatField(widget=forms.HiddenInput)
    contents = forms.CharField(widget=forms.TextInput, label="Please describe what happened", required=True)
    captcha = ReCaptchaField(widget = ReCaptchaV3)


    def clean(self):
        cd = self.cleaned_data

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
