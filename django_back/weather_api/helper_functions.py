from geopy.geocoders import Nominatim
import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

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
    print(f"Coordinates {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation {response.Elevation()} m asl")
    print(f"Timezone {response.Timezone()} {response.TimezoneAbbreviation()}")
    print(f"Timezone difference to GMT+0 {response.UtcOffsetSeconds()} s")

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
        hourly_data[variable_name] = response.Hourly().Variables(i).ValuesAsNumpy()

    hourly_dataframe = pd.DataFrame(data=hourly_data)
    return hourly_dataframe
