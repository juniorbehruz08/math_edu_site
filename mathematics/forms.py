from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=16, help_text='Maximum 16 Character',
                               widget=forms.TextInput(attrs={
                                   'placeholder': 'Username'
                               }))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={
                                   'placeholder': 'Password'
                               })
                               )


class RegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded',
        'name': 'username',
        'placeholder': 'Username ( Iloji boricha son va belgilardan foydalaning )'
    }))
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded',
        'name': 'first_name',
        'placeholder': 'First Name ( Belgilar va sonlarni ishlatmang!!! )'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control rounded',
        'name': 'last_name',
        'placeholder': 'Last Name ( Belgilar va sonlarni ishlatmang!!! )'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control rounded',
        'name': 'email',
        'placeholder': 'Email'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded',
        'name': 'password1',
        'placeholder': 'Password ( Kamida 8 ta belgi harflar, sonlar va belgilardan qatnashtirish talab etiladi )'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control rounded',
        'name': 'password2',
        'placeholder': 'Return Password ( Parolni takrorlang )'
    }))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )


class ProfileCreation(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture',
            'user',
            'language'
        ]
