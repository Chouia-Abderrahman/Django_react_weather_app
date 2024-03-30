from django_cron import CronJobBase, Schedule
from .views import fetch_weather_data

class FetchWeatherDataCron(CronJobBase):
    schedule = Schedule(run_every_mins=1440)
    code = 'weather_api.fetch_weather_data'

    def do(self):
        fetch_weather_data(None)
