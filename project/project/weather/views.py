from django.shortcuts import render
# Create your views here.
from project.weather.forms import GetCityForm, GetZodiacSignForm
from project.weather.models import City, Weather, ZodiacSigns


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


def display_zodiacs_view(request):
    zodiac_sign = None

    if request.method == "POST":
        form = GetZodiacSignForm(request.POST)
        if form.is_valid():
            zodiac_sign = ZodiacSigns.objects.get(name=form.cleaned_data['name'])
    else:
        form = GetZodiacSignForm()

    context = {
        'form': form,
        'zodiac_sign': zodiac_sign,
    }

    return render(request, 'weather/displey-zodiacs.html', context)
