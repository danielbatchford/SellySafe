from django import forms
from django.core.exceptions import ValidationError

from SellySafe import settings
from .models import Report, Feedback

# Custom Datetime Widget to use HTML5 Datetime picker
class DateTimeInput(forms.DateInput):
    input_type = 'datetime-local'

    def __init__(self, **kwargs):
        # Use datetime format from Django Settings
        kwargs["format"] = settings.DATETIME_INPUT_FORMATS[0]

        super().__init__(**kwargs)


# Report form to add a new report
class ReportForm(forms.Form):

    # Choices for datetime options
    CHOICES = [(0, 'Just now'),
               (5, '5 minutes ago'),
               (15, '15 minutes ago'),
               (30, '30 minutes ago'),
               (1, '1 hour ago'),
               (2, '2 hours ago'),
               (3, '3 hours ago'),
               (4, '4 hours ago')]

    datetime = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect, label="When did this happen?",
                                 required=True, initial=0)

    # Define hidden inputs not shown to the user. Lat and Long are set through JS when a user clicks on the map.
    lat = forms.FloatField(widget=forms.HiddenInput)
    long = forms.FloatField(widget=forms.HiddenInput)

    contents = forms.CharField(widget=forms.TextInput, label="Please describe what happened", required=True)

    # Clean data on a submitted form
    def clean(self):
        cd = self.cleaned_data

        bounds = settings.BOUNDS
        bl = bounds[0]
        tr = bounds[1]

        # Check if submitted Lat / Long is within defined map bounds. (To prevent malicious post form requests)
        if cd['long'] > tr[0] or cd['long'] < bl[0]:
            raise ValidationError("Longitude out of bounds")
        if cd['lat'] > tr[1] or cd['lat'] < bl[1]:
            raise ValidationError("Latitude out of bounds")

    class Meta:
        model = Report
        fields = ("contents", "lat", "long", "datetime")


# Feedback form for users to submit feedback
class FeedbackForm(forms.ModelForm):
    contents = forms.CharField(required=True, label="Please enter your feedback below")
    email = forms.CharField(required=False, label="Email (Optional), to allow us to get in touch")

    class Meta:
        model = Feedback
        fields = ("contents", "email")
