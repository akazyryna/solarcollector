from django import forms
from django.core.exceptions import ValidationError
from .constants import MONTHS
from .models import City


class FilterForm(forms.Form):
    city = forms.ChoiceField(choices=City.objects.choices(), widget=forms.Select(attrs={'class': 'form-control'}))
    month_from = forms.ChoiceField(choices=MONTHS, widget=forms.Select(attrs={'class': 'form-control'}))
    month_to = forms.ChoiceField(choices=MONTHS, widget=forms.Select(attrs={'class': 'form-control'}))
    incn_angle = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'The angle of inclination of the CSE to the horizon'}))

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['month_from'] > cleaned_data['month_to']:
            raise ValidationError({'month_to': "Must be greater than month from"})
        return cleaned_data
