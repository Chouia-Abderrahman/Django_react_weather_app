# news_api_proxy/urls.py

from django.urls import path
from .views import current_day_weather, current_day_weather_with_location, create_location
# from views import function_its_calling

urlpatterns = [
    # path('url-endpoint-name/', function_its_calling, name='fetch_news'),
    path('current/', current_day_weather, name='current_day_weather'),
    path('current/<str:location>/', current_day_weather_with_location, name='current_day_weather_with_location'),
    path('locations/', create_location, name='create_location'),
]