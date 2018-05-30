from django.shortcuts import render
from django.views import View

from . import models, formulas
from .forms import FilterForm


class IndexView(View):
    def get(self, request):
        return render(request, template_name='main/index.html',
                      context={'filter_form': FilterForm()})

    def post(self, request):
        filter_form = FilterForm(request.POST)

        if not filter_form.is_valid():
            return render(request, template_name='main/index.html',
                          context={'filter_form': filter_form})


        props = models.Property.objects.filter(city__id = filter_form.cleaned_data['city'],
                                                    month__in=[filter_form.cleaned_data['month_from'],
                                                               filter_form.cleaned_data['month_to']])

        city_props = models.CityProperty.objects.filter(city__id = filter_form.cleaned_data['city'])

        return render(request, template_name='main/index.html',
                      context={'filter_form': filter_form,
                               'properties': props, 'city_properties': city_props,
                               'months': [filter_form.cleaned_data['month_from'],
                                          filter_form.cleaned_data['month_to']]})
