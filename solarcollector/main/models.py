from django.db import models


class CitiesManager(models.Manager):
    def choices(self):
        return tuple((city.id, city.name) for city in self.all().iterator())


class City(models.Model):
    name = models.CharField(max_length=20)

    objects = CitiesManager()


class CityProperty(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    value = models.FloatField()
    type = models.IntegerField(blank=True, null=True)


class Property(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    value = models.FloatField()
    month = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
