from django import forms
from .models import Profile
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=50)
    email_address = forms.EmailField(max_length=50)
    address = forms.CharField(max_length=200)

    class Meta:
        model = Profile
        fields = "__all__"
