from django.shortcuts import render
from django.views import generic as views

# Create your views here.
from project.weather.forms import GetCityForm
from project.weather.models import City


def display_weather_view(request):
    form = GetCityForm(request.GET)
    city = City.objects.get(name__exact=)

    context = {
        'form': form,
        'city': city,
    }

    return render(request, 'weather/dislpay-weather.html', context)
