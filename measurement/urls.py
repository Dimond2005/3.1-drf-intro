from django.urls import path

from measurement.serializers import SensorDetailSerializer
from measurement.views import SensorsView, SensorsNumberView, MeasurementsView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorsNumberView.as_view()),
    path('measurements/', MeasurementsView.as_view())
]
