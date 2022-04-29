import cloudinary
from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.
from project.common.validators import validate_only_percentage


class Weather(models.Model):
    temperature = models.IntegerField()

    humidity = models.IntegerField(
        validators=(
            validate_only_percentage,
        )
    )

    wind = models.IntegerField()

    probability_for_rain = models.IntegerField(
        validators=(
            validate_only_percentage,
        )
    )


class City(models.Model):
    SOFIA = 'Sofia'
    PLOVDIV = 'Plovdiv'
    VARNA = 'Varna'
    BURGAS = 'Burgas'
    RAZGRAD = 'Razgrad'

    CITIES = [(x, x) for x in (SOFIA, PLOVDIV, VARNA, BURGAS, RAZGRAD)]

    name = models.CharField(
        max_length=max(len(x) for x, _ in CITIES),
        choices=CITIES,
    )

    Weather = models.ForeignKey(
        Weather,
        on_delete=models.CASCADE,
    )


class ZodiacSigns(models.Model):
    MAX_DATE_LENGTH = 100
    MAX_ELEMENT_LENGTH = 50
    MAX_RULING_PLANET_LENGTH = 50

    ARIES = 'Aries'
    TAURUS = 'Taurus'
    GEMINI = 'Gemini'
    CANCER = 'Cancer'
    LEO = 'Leo'
    VIRGO = 'Virgo'
    LIBRA = 'Libra'
    SCORPIO = 'Scorpio'
    SAGITTARIUS = 'Sagittarius'
    CAPRICORN = 'Capricorn'
    AQUARIUS = 'Aquarius'
    PISCES = 'Pisces'

    ZODIACS = [(x, x) for x in (ARIES, TAURUS, GEMINI, CANCER, LEO, VIRGO, LIBRA, SCORPIO, SAGITTARIUS, CAPRICORN, AQUARIUS, PISCES)]

    name = models.CharField(
        max_length=max(len(x) for x, _ in ZODIACS),
        choices=ZODIACS,
    )

    date = models.CharField(
        max_length=MAX_DATE_LENGTH,
    )

    element = models.CharField(
        max_length=MAX_ELEMENT_LENGTH,
    )

    ruling_planet = models.CharField(
        max_length=MAX_RULING_PLANET_LENGTH,
    )

    personal_traits = models.TextField()

    image = CloudinaryField('image')
