from django.urls import path, reverse_lazy
from project.weather.views import display_weather_view

urlpatterns = [
    path('', display_weather_view, name='display weather'),
]