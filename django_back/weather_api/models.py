from django.db import models


class Location(models.Model):

    location_name = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.location_name

class HourlyWeatherData(models.Model):

    location_name = models.ForeignKey(Location, on_delete=models.CASCADE)
    date_time = models.DateTimeField(null=False)
    temperature_2m = models.FloatField()
    relative_humidity_2m = models.FloatField()
    dew_point_2m = models.FloatField()
    apparent_temperature = models.FloatField()
    precipitation = models.FloatField()
    rain = models.FloatField()
    showers = models.FloatField()
    snowfall = models.FloatField()
    snow_depth = models.FloatField()
    weather_code = models.FloatField()
    pressure_msl = models.FloatField()
    surface_pressure = models.FloatField()
    cloud_cover = models.FloatField()
    cloud_cover_low = models.FloatField()
    cloud_cover_mid = models.FloatField()
    cloud_cover_high = models.FloatField()
    visibility = models.FloatField()
    et0_fao_evapotranspiration = models.FloatField()
    vapour_pressure_deficit = models.FloatField()
    wind_speed_10m = models.FloatField()
    wind_speed_30m = models.FloatField()
    wind_speed_50m = models.FloatField()
    wind_speed_70m = models.FloatField()
    wind_speed_100m = models.FloatField()
    wind_speed_120m = models.FloatField()
    wind_speed_140m = models.FloatField()
    wind_speed_160m = models.FloatField()
    wind_speed_180m = models.FloatField()
    wind_speed_200m = models.FloatField()
    wind_direction_10m = models.FloatField()
    wind_direction_30m = models.FloatField()
    wind_direction_50m = models.FloatField()
    wind_direction_70m = models.FloatField()
    wind_direction_100m = models.FloatField()
    wind_direction_120m = models.FloatField()
    wind_direction_140m = models.FloatField()
    wind_direction_160m = models.FloatField()
    wind_direction_180m = models.FloatField()
    wind_direction_200m = models.FloatField()
    wind_gusts_10m = models.FloatField()
    surface_temperature = models.FloatField()
    soil_temperature_0_to_10cm = models.FloatField()
    soil_temperature_10_to_40cm = models.FloatField()
    soil_temperature_40_to_100cm = models.FloatField()
    soil_temperature_100_to_200cm = models.FloatField()
    soil_moisture_0_to_10cm = models.FloatField()
    soil_moisture_10_to_40cm = models.FloatField()
    soil_moisture_40_to_100cm = models.FloatField()
    soil_moisture_100_to_200cm = models.FloatField()
    is_day = models.BinaryField()
    sunshine_duration = models.FloatField()
    cape = models.FloatField()
    lifted_index = models.FloatField()
    convective_inhibition = models.FloatField()

    def __str__(self):
        return f"{self.location_name} {self.date_time}"
    class Meta:
        db_table = 'hourly_weather_data'
