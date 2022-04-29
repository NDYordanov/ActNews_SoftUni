from django.shortcuts import render
# Create your views here.
from project.weather.forms import GetCityForm
from project.weather.models import City, Weather


def display_weather_view(request):
    city = None
    weather = None

    if request.method == "POST":
        form = GetCityForm(request.POST)
        if form.is_valid():
            city = City.objects.get(name=form.cleaned_data['name'])
            weather = city.Weather

    else:
        form = GetCityForm()

    context = {
        'form': form,
        'city': city,
        'weather': weather,
    }

    return render(request, 'weather/dislpay-weather.html', context)
