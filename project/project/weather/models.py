from django.db import models

# Create your models here.
from project.common.validators import validate_only_letters


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
