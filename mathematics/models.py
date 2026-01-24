from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


class Languages(models.Model):
    language = models.CharField(max_length=50, verbose_name='Language')

    def __str__(self):
        return self.language

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='profile_photo/', verbose_name='photo', blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile_settings')
    language = models.ForeignKey(Languages, on_delete=models.CASCADE, default=1)

    def get_photo(self):
        if self.profile_picture:
            return self.profile_picture.url
        else:
            return '/static/images/myimages/profile.jpg'

    def __str__(self):
        return self.language.language

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
