# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from datetime import datetime
from measurement.models import Sensor, Measurement
from measurement.serializers import SensorDetailSerializer, MeasurementSerializer
from rest_framework.response import Response


class SensorsView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        serialaizer = SensorDetailSerializer(sensors,  many=True)
        return Response(serialaizer.data)

    def post(self, request):
        Sensor(name=request.data.get('name'), description=request.data.get('description')).save()
        return Response({'status': 'OK'})

    def patch(self, request):
        Sensor(name=request.data.get('name'), description=request.data.get('description')).save()
        return Response({'status': 'OK'})


class MeasurementsView(APIView):
    def get(self, request):
        measurement = Measurement.objects.all()
        serialaizer = MeasurementSerializer(measurement, many=True)
        return Response(serialaizer.data)

    def post(self, request):
        Measurement(id=request.data.get('sensor'), temperature=request.data.get('temperature'),
                    created_at=datetime.now()).save()
        return Response({'status': 'OK'})

    def patch(self, request):
        Measurement(id=request.data.get('sensor'), temperature=request.data.get('temperature'),
                    created_at=datetime.now()).save()
        return Response({'status': 'OK'})


class SensorsNumberView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
