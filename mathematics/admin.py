from django.contrib import admin
from .models import *


@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'language',)
    list_display_links = ('language',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'language')
    list_display_links = ('language',)


