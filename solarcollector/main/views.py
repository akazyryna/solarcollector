from django.shortcuts import render
from django.views import View

from . import reports, constants
from .forms import FilterForm


class IndexView(View):
    def get(self, request):
        return render(request, template_name='main/index.html',
                      context={'filter_form': FilterForm()})


class FilterView(View):
    def post(self, request):
        filter_form = FilterForm(request.POST)

        context = {
            'filter_form': filter_form}

        if filter_form.is_valid():
            incn_angle = filter_form.cleaned_data['incn_angle']
            month_from = int(filter_form.cleaned_data['month_from'])
            month_to = int(filter_form.cleaned_data['month_to'])
            months = range(month_from, month_to + 1) if month_to else [month_from]
            report = reports.MainCitiesMonthsReport([filter_form.cleaned_data['city']], months, incn_angle)

            context.update({'report': report,
                            'MONTHS': dict(constants.MONTHS)})

        return render(request, template_name='main/index.html', context=context)
