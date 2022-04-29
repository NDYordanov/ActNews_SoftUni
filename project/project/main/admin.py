from django.contrib import admin

# Register your models here.
from project.accounts.models import Profile, ActNewsUser
from project.main.models import Article
from project.weather.models import Weather, City


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(ActNewsUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'username')


@admin.register(Article)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Weather)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('temperature',)


@admin.register(City)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name',)
