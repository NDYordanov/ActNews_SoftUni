from django import forms

from project.weather.models import City


class GetCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
