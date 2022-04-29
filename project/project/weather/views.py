from django.shortcuts import render
from django.views import generic as views

# Create your views here.
from project.weather.forms import GetCityForm
from project.weather.models import City


def display_weather_view(request):
    city = None

    if request.method == "POST":
        form = GetCityForm(request.POST)
        if form.is_valid():
            city = City.objects.get(name=form.cleaned_data['name'])
    else:
        form = GetCityForm()

    context = {
        'form': form,
        'city': city,
    }

    return render(request, 'weather/dislpay-weather.html', context)
