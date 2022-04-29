import cloudinary
from cloudinary import models as cloudinary_model
from django.contrib.auth import get_user_model
from django.db import models

from project.accounts.models import Profile

UserModel = get_user_model()


# Create your models here.
class Article(models.Model):
    MAX_TITLE_LENGTH = 50

    SPORTS = 'Sports'
    ECONOMICS = 'Economics'
    CORONAVIRUS = 'Coronavirus'
    POLITICS = 'Politics'

    CATEGORIES = [(x, x) for x in (SPORTS, ECONOMICS, CORONAVIRUS, POLITICS)]

    title = models.CharField(
        max_length=MAX_TITLE_LENGTH,
    )

    category = models.CharField(
        max_length=max(len(x) for x, _ in CATEGORIES),
        choices=CATEGORIES,
    )

    image = cloudinary_model.CloudinaryField('image')

    date = models.DateTimeField(
        auto_now_add=True,
    )

    summary = models.TextField()

    journalist = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-date']