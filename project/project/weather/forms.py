from django import forms

from project.weather.models import City, ZodiacSigns


class GetCityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']


class GetZodiacSignForm(forms.ModelForm):
    class Meta:
        model = ZodiacSigns
        fields = ['name']
