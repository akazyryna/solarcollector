from django import forms

from .constants import MONTHS
from .models import City


class FilterForm(forms.Form):
    city = forms.ChoiceField(choices=City.objects.choices())
    month_from = forms.ChoiceField(choices=MONTHS)
    month_to = forms.ChoiceField(choices=MONTHS)

