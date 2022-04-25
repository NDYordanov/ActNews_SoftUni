from django.contrib import admin

# Register your models here.
from project.accounts.models import Profile
from project.main.models import Article


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Article)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('title', )
