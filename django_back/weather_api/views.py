from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import HourlyWeatherData, Location
from .helper_functions import get_weather_info, get_coordinates, fetch_and_insert_weather_data_to_db
from datetime import datetime, date
from .serializers import HourlyWeatherDataSerializer, LocationSerializer
from django.utils import timezone

@api_view(['GET'])
def fetch_weather_data(request):
    # fetching all records in the database
    all_locations = Location.objects.all()
    for location in all_locations:
        lat, lon = get_coordinates(location)
        weather_info_dataframe = get_weather_info(lat, lon)

        for _, row in weather_info_dataframe.iterrows():
            hourly_weather_data = HourlyWeatherData()
            for col_name in weather_info_dataframe.columns:
                setattr(hourly_weather_data, col_name, row[col_name])

                # Save the HourlyWeatherData object to the database
            hourly_weather_data.save()

    return Response({'message': 'Weather data updated successfully'})

@api_view(['GET'])
def current_day_weather(request):
    return Response({'message': 'current_day_weather'})

@api_view(['GET'])
def current_day_weather_with_location(request, location):

    # location_rec = Location.objects.get(name=location)
    try:
        location_rec = Location.objects.get(name=location)
    except Exception:
        location_rec = Location.objects.create(name=location)
        location_rec.save()
        fetch_and_insert_weather_data_to_db(location_rec)

    if not HourlyWeatherData.objects.filter(location_name_id=location_rec.id, date_time__date=timezone.now().date()):
        fetch_and_insert_weather_data_to_db(location_rec)

    print(timezone.now().date())
    result_weather_data = HourlyWeatherData.objects.filter(
        location_name_id=location_rec.id,
        date_time__date=timezone.now().date()
    )

    # print(result_weather_data)
    serializer = HourlyWeatherDataSerializer(result_weather_data, many=True)
    # print(serializer.data)
    return Response(serializer.data)
