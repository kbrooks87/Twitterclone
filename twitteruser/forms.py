from django import forms
from django.contrib.auth.forms import UserCreationForm
from twitteruser.models import TwitterUser


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = TwitterUser
        fields = ['username', 'email', 'password1']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = TwitterUser
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = TwitterUser
        fields = ['image']
