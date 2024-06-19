from rest_framework import serializers
from .models import HourlyWeatherData, Location


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class HourlyWeatherDataSerializer(serializers.ModelSerializer):
    location_id = LocationSerializer(read_only=True)
    class Meta:
        model = HourlyWeatherData
        fields = '__all__'
