from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth import models as auth_models, get_user_model
from project.accounts.managers import ActNewsUserManager
#from project.main.models import Article
from cloudinary import models as cloudinary_model

from project.common.validators import validate_only_letters


class ActNewsUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 30

    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = ActNewsUserManager()


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30

    JOURNALIST = 'Journalist'
    SITE_DEVELOPER = 'Site developer'
    PUBLIC_MEMBER = 'Public member'
    DIRECTOR = 'Director'

    CATEGORIES = [(x, x) for x in (JOURNALIST, SITE_DEVELOPER, PUBLIC_MEMBER, DIRECTOR)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validate_only_letters,
        )
    )

    position = models.CharField(
        max_length=max(len(x) for x, _ in CATEGORIES),
        choices=CATEGORIES,
    )

    profile_picture = cloudinary_model.CloudinaryField('image')

    user = models.ForeignKey(
        ActNewsUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    # article = models.ForeignKey(
    #     Article,
    #     on_delete=models.CASCADE,
    # )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
