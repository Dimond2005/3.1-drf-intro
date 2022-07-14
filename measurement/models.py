from django.db import models


# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=20)


class Measurement(models.Model):
    temperature = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
