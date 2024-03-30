from django.db import models


class Location(models.Model):

    name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.name

class HourlyWeatherData(models.Model):

    location_name = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=True)
    temperature_2m = models.FloatField(null=True)
    relative_humidity_2m = models.FloatField(null=True)
    dew_point_2m = models.FloatField(null=True)
    apparent_temperature = models.FloatField(null=True)
    precipitation = models.FloatField(null=True)
    rain = models.FloatField(null=True)
    showers = models.FloatField(null=True)
    snowfall = models.FloatField(null=True)
    snow_depth = models.FloatField(null=True)
    weather_code = models.FloatField(null=True)
    pressure_msl = models.FloatField(null=True)
    surface_pressure = models.FloatField(null=True)
    cloud_cover = models.FloatField(null=True)
    cloud_cover_low = models.FloatField(null=True)
    cloud_cover_mid = models.FloatField(null=True)
    cloud_cover_high = models.FloatField(null=True)
    visibility = models.FloatField(null=True)
    et0_fao_evapotranspiration = models.FloatField(null=True)
    vapour_pressure_deficit = models.FloatField(null=True)
    wind_speed_10m = models.FloatField(null=True)
    wind_speed_30m = models.FloatField(null=True)
    wind_speed_50m = models.FloatField(null=True)
    wind_speed_70m = models.FloatField(null=True)
    wind_speed_100m = models.FloatField(null=True)
    wind_speed_120m = models.FloatField(null=True)
    wind_speed_140m = models.FloatField(null=True)
    wind_speed_160m = models.FloatField(null=True)
    wind_speed_180m = models.FloatField(null=True)
    wind_speed_200m = models.FloatField(null=True)
    wind_direction_10m = models.FloatField(null=True)
    wind_direction_30m = models.FloatField(null=True)
    wind_direction_50m = models.FloatField(null=True)
    wind_direction_70m = models.FloatField(null=True)
    wind_direction_100m = models.FloatField(null=True)
    wind_direction_120m = models.FloatField(null=True)
    wind_direction_140m = models.FloatField(null=True)
    wind_direction_160m = models.FloatField(null=True)
    wind_direction_180m = models.FloatField(null=True)
    wind_direction_200m = models.FloatField(null=True)
    wind_gusts_10m = models.FloatField(null=True)
    surface_temperature = models.FloatField(null=True)
    soil_temperature_0_to_10cm = models.FloatField(null=True)
    soil_temperature_10_to_40cm = models.FloatField(null=True)
    soil_temperature_40_to_100cm = models.FloatField(null=True)
    soil_temperature_100_to_200cm = models.FloatField(null=True)
    soil_moisture_0_to_10cm = models.FloatField(null=True)
    soil_moisture_10_to_40cm = models.FloatField(null=True)
    soil_moisture_40_to_100cm = models.FloatField(null=True)
    soil_moisture_100_to_200cm = models.FloatField(null=True)
    sunshine_duration = models.FloatField(null=True)
    is_day = models.BooleanField(null=True)
    cape = models.FloatField(null=True)
    lifted_index = models.FloatField(null=True)
    convective_inhibition = models.FloatField(null=True)

    def __str__(self):
        return f"{self.location_name} {self.date_time}"
    class Meta:
        db_table = 'hourly_weather_data'
