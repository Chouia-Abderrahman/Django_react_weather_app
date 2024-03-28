from rest_framework import serializers
from .models import HourlyWeatherData, Location

class HourlyWeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourlyWeatherData
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'