from django.db import models


class HistoricPlaces(models.Model):
    title = models.CharField(verbose_name='título', max_length=50)
    description = models.CharField(verbose_name='descrição', max_length=250)
    latitude = models.FloatField(verbose_name='latitude')
    longitude = models.FloatField(verbose_name='longitude')

    def __str__(self):
        return self.title
