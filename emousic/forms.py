from django import forms
from django.core.validators import FileExtensionValidator

CHOICES = [(0, 'Arithmetic mean'), (1, 'Weighted mean'), (2, 'Majority')]


class TrackForm(forms.Form):
    file = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['midi', 'mid'])])
    approach = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
