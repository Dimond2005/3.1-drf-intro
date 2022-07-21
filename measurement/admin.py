from django.contrib import admin

# Register your models here.
from measurement.models import Sensor, Measurement


class MeasurementInline(admin.TabularInline):
    model = Measurement


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    inlines = [MeasurementInline, ]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'temperature', 'created_at', 'sensor']
