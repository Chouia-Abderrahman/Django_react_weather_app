from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import HourlyWeatherData, Location
from .helper_functions import get_weather_info, get_coordinates, fetch_and_insert_weather_data_to_db
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

@api_view(['POST'])
def create_location(request):
    serializer = LocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def current_day_weather_with_location(request, location):
    """
    Get current day weather data for a specific location.
    Args:
        request (HttpRequest): The HTTP request object.
        location (str): The name of the location for which weather data is requested.

    Returns:
        Response: A JSON response containing weather data for the current day at the specified location.
    """
    try:
        location_rec = Location.objects.get(name=location)
    except Exception:
        location_rec = Location.objects.create(name=location)
        location_rec.save()
        fetch_and_insert_weather_data_to_db(location_rec)

    if not HourlyWeatherData.objects.filter(location_id=location_rec.id,
                                            date_time__date=timezone.now().date()):
        fetch_and_insert_weather_data_to_db(location_rec)

    result_weather_data = HourlyWeatherData.objects.filter(
        location_id=location_rec.id,
        date_time__date=timezone.now().date()
    )
    serializer = HourlyWeatherDataSerializer(result_weather_data, many=True)
    return Response(serializer.data)
