from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import CustomUser


class CustomUserSignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2', )


class CustomUserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'birthday', ]
