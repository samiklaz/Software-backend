from django.db import models


class Cases(models.Model):
    confirmed = models.IntegerField(blank=True, null=True)
    recovered = models.IntegerField(blank=True, null=True)
    deaths = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    sq_km_area = models.IntegerField(blank=True, null=True)
    life_expectancy = models.CharField(max_length=255, blank=True, null=True)
    elevation_in_meters = models.CharField(max_length=255, blank=True, null=True)
    continent = models.CharField(max_length=255, blank=True, null=True)
    abbreviation = models.CharField(max_length=25, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    capital_city = models.CharField(max_length=255, blank=True, null=True)
    lat = models.CharField(max_length=25, blank=True, null=True)
    long = models.CharField(max_length=25, blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Cases'

    def __str__(self):
        return str(self.country)
