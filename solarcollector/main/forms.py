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

    '''
    cold_temp = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Сold water temperature'}))
    daily_dis = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Daily hot water consumption'}))
    optical_efficiency = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Effective optical efficiency'}))
    length_pipe = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Panel and pipe length, in meters'}))
    channel_height = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'The height of the coolant channel, in meters'}))
    plate_thickness = forms.FloatField(localize=True, widget=forms.NumberInput(
         attrs={'class': 'form-control', 'placeholder': 'Plate wall thickness, in meters'}))
    surface_thickness = forms.FloatField(localize=True, widget=forms.NumberInput(
         attrs={'class': 'form-control', 'placeholder': 'Thickness of the translucent surface, in meters'}))
    area = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'The area of the illuminated surface'}))
    inhabitant = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Number of inhabitants'}))
    efficiency = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'The initial efficiency of the solar collector'}))
    temp_glass = forms.FloatField(localize=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'The initial temperature of the glass'}))
    '''

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data['month_from'] > cleaned_data['month_to']:
            raise ValidationError({'month_to': "Must be greater than month from"})
        return cleaned_data
