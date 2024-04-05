from geopy.geocoders import Nominatim
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry
import numpy as np
from .models import HourlyWeatherData, Location

def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(location_name)

    if location:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None, None

def get_weather_info(lat, lon, number_of_days=16):
    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
    retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
    openmeteo = openmeteo_requests.Client(session=retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/cma"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ["temperature_2m", "relative_humidity_2m", "dew_point_2m", "apparent_temperature", "precipitation",
                   "rain", "showers", "snowfall", "snow_depth", "weather_code", "pressure_msl", "surface_pressure",
                   "cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high", "visibility",
                   "et0_fao_evapotranspiration", "vapour_pressure_deficit", "wind_speed_10m", "wind_speed_30m",
                   "wind_speed_50m", "wind_speed_70m", "wind_speed_100m", "wind_speed_120m", "wind_speed_140m",
                   "wind_speed_160m", "wind_speed_180m", "wind_speed_200m", "wind_direction_10m", "wind_direction_30m",
                   "wind_direction_50m", "wind_direction_70m", "wind_direction_100m", "wind_direction_120m",
                   "wind_direction_140m", "wind_direction_160m", "wind_direction_180m", "wind_direction_200m",
                   "wind_gusts_10m", "surface_temperature", "soil_temperature_0_to_10cm", "soil_temperature_10_to_40cm",
                   "soil_temperature_40_to_100cm", "soil_temperature_100_to_200cm", "soil_moisture_0_to_10cm",
                   "soil_moisture_10_to_40cm", "soil_moisture_40_to_100cm", "soil_moisture_100_to_200cm", "is_day",
                   "sunshine_duration", "cape", "lifted_index", "convective_inhibition"],
        "timezone": "auto",
        "forecast_days": number_of_days,
    }
    responses = openmeteo.weather_api(url, params=params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    # print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    # print(f"Elevation {response.Elevation()} m asl")
    # print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    # print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

    # Process hourly data directly without storing them in separate variables
    hourly_data = {
        "date": pd.date_range(
            start=pd.to_datetime(response.Hourly().Time(), unit="s", utc=True),
            end=pd.to_datetime(response.Hourly().TimeEnd(), unit="s", utc=True),
            freq=pd.Timedelta(seconds=response.Hourly().Interval()),
            inclusive="left"
        )
    }

    # Assign hourly data directly to hourly_data dictionary
    for i, variable_name in enumerate(params["hourly"]):
        # hourly_data[variable_name] = response.Hourly().Variables(i).ValuesAsNumpy()
        values = response.Hourly().Variables(i).ValuesAsNumpy()
        values_without_nans = np.nan_to_num(values, nan=0.0)  # Replace NaNs with 0.0
        hourly_data[variable_name] = values_without_nans
    hourly_dataframe = pd.DataFrame(data=hourly_data)
    hourly_dataframe['is_day'] = hourly_dataframe['is_day'].astype(int)
    return hourly_dataframe

def fetch_and_insert_weather_data_to_db(location_rec):
    lat, lon = get_coordinates(location_rec.name)
    weather_info_dataframe = get_weather_info(lat, lon)
    print(len(weather_info_dataframe), weather_info_dataframe)
    for _, row in weather_info_dataframe.iterrows():
        hourly_weather_data = HourlyWeatherData()
        hourly_weather_data.location_name = location_rec
        hourly_weather_data.date_time = row['date']
        hourly_weather_data.temperature_2m = row['temperature_2m']
        hourly_weather_data.relative_humidity_2m = row['relative_humidity_2m']
        hourly_weather_data.dew_point_2m = row['dew_point_2m']
        hourly_weather_data.apparent_temperature = row['apparent_temperature']
        hourly_weather_data.precipitation = row['precipitation']
        hourly_weather_data.rain = row['rain']
        hourly_weather_data.showers = row['showers']
        hourly_weather_data.snowfall = row['snowfall']
        hourly_weather_data.snow_depth = row['snow_depth']
        hourly_weather_data.weather_code = row['weather_code']
        hourly_weather_data.pressure_msl = row['pressure_msl']
        hourly_weather_data.surface_pressure = row['surface_pressure']
        hourly_weather_data.cloud_cover = row['cloud_cover']
        hourly_weather_data.cloud_cover_low = row['cloud_cover_low']
        hourly_weather_data.cloud_cover_mid = row['cloud_cover_mid']
        hourly_weather_data.cloud_cover_high = row['cloud_cover_high']
        hourly_weather_data.visibility = row['visibility']
        hourly_weather_data.et0_fao_evapotranspiration = row['et0_fao_evapotranspiration']
        hourly_weather_data.vapour_pressure_deficit = row['vapour_pressure_deficit']
        hourly_weather_data.wind_speed_10m = row['wind_speed_10m']
        hourly_weather_data.wind_speed_30m = row['wind_speed_30m']
        hourly_weather_data.wind_speed_50m = row['wind_speed_50m']
        hourly_weather_data.wind_speed_70m = row['wind_speed_70m']
        hourly_weather_data.wind_speed_100m = row['wind_speed_100m']
        hourly_weather_data.wind_speed_120m = row['wind_speed_120m']
        hourly_weather_data.wind_speed_140m = row['wind_speed_140m']
        hourly_weather_data.wind_speed_160m = row['wind_speed_160m']
        hourly_weather_data.wind_speed_180m = row['wind_speed_180m']
        hourly_weather_data.wind_speed_200m = row['wind_speed_200m']
        hourly_weather_data.wind_direction_10m = row['wind_direction_10m']
        hourly_weather_data.wind_direction_30m = row['wind_direction_30m']
        hourly_weather_data.wind_direction_50m = row['wind_direction_50m']
        hourly_weather_data.wind_direction_70m = row['wind_direction_70m']
        hourly_weather_data.wind_direction_100m = row['wind_direction_100m']
        hourly_weather_data.wind_direction_120m = row['wind_direction_120m']
        hourly_weather_data.wind_direction_140m = row['wind_direction_140m']
        hourly_weather_data.wind_direction_160m = row['wind_direction_160m']
        hourly_weather_data.wind_direction_180m = row['wind_direction_180m']
        hourly_weather_data.wind_direction_200m = row['wind_direction_200m']
        hourly_weather_data.wind_gusts_10m = row['wind_gusts_10m']
        hourly_weather_data.surface_temperature = row['surface_temperature']
        hourly_weather_data.soil_temperature_0_to_10cm = row['soil_temperature_0_to_10cm']
        hourly_weather_data.soil_temperature_10_to_40cm = row['soil_temperature_10_to_40cm']
        hourly_weather_data.soil_temperature_40_to_100cm = row['soil_temperature_40_to_100cm']
        hourly_weather_data.soil_temperature_100_to_200cm = row['soil_temperature_100_to_200cm']
        hourly_weather_data.soil_moisture_0_to_10cm = row['soil_moisture_0_to_10cm']
        hourly_weather_data.soil_moisture_10_to_40cm = row['soil_moisture_10_to_40cm']
        hourly_weather_data.soil_moisture_40_to_100cm = row['soil_moisture_40_to_100cm']
        hourly_weather_data.soil_moisture_100_to_200cm = row['soil_moisture_100_to_200cm']
        hourly_weather_data.is_day = row['is_day']
        hourly_weather_data.sunshine_duration = row['sunshine_duration']
        hourly_weather_data.cape = row['cape']
        hourly_weather_data.lifted_index = row['lifted_index']
        hourly_weather_data.convective_inhibition = row['convective_inhibition']
        # hourly_weather_data.location_name = location_

        # print(weather_info_dataframe.columns)

        # for col_name in weather_info_dataframe.columns:
        #     setattr(hourly_weather_data, col_name, row[col_name])

        saved = hourly_weather_data.save()
        # print(saved)