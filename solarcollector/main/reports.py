from . import models, formulas


class BaseReport:
    def report_values(self, *args, **kwargs):
        raise NotImplementedError()


class MainCitiesMonthsReport(BaseReport):
    def __init__(self, cities_ids, months, incn_angle):
        self.cities_ids = cities_ids
        self.months = months
        self.incn_angle = incn_angle

    def report_values(self):
        _report_values = []

        try:
            for city_id in self.cities_ids:
                _report_values.append({
                    'city': models.City.objects.get(id=city_id),
                    'months_report': {month: self._city_properties_per_month(city_id, month) for month in self.months},
                    'incn_angle': self.incn_angle
                })
        except models.City.DoesNotExist:
            pass

        return _report_values

    def _city_properties_per_month(self, city_id, month):
        props = models.Property.objects.as_dict(city__id=city_id, month=month)
        cities_props = models.CityProperty.objects.as_dict(city__id=city_id)
        self.incn_angle = self.incn_angle
        for_horizontal = formulas.formula_for_horizontal(cities_props['lat'].value, props['horz_angle'].value)
        for_inclination = formulas.formula_for_inclination(cities_props['lat'].value, props['horz_angle'].value,
                                                           self.incn_angle)
        for_min = formulas.formula_min(for_horizontal, for_inclination)
        conversion_factor = formulas.formula_conversion_factor(cities_props['lat'].value, self.incn_angle, for_min,
                                                               props['horz_angle'].value, for_horizontal)
        convers = formulas.formula_convers(self.incn_angle, props['ed'].value, props['e'].value, conversion_factor,
                                         cities_props['ro'].value)
        amount_energy = formulas.formula_amount_energy(convers, props['e'].value)

        try:
            return [
                for_horizontal,
                for_min,
                conversion_factor,
                convers,
                amount_energy
            ]
        except KeyError:
            return []
