from django.shortcuts import render
from django.contrib.auth.models import auth
# from django.contrib.auth.models import User
from django.contrib import messages
from .models import Profile
from .form import ProfileForm


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'dashboard.html', {})
        else:
            messages.info(request, 'Wrong username and password')
    else:
        return render(request, 'login.html', {})


def home_page(request, *args, **kwargs):
    return render(request, 'dashboard.html', {})


def reset_pass(request, *args, **kwargs):
    return render(request, 'recovery_pass.html', {})


def create_profile(request, *args, **kwargs):
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST)
        if prof_form.is_valid():
            prof_form.save(commit=True)
    form = ProfileForm()
    return render(request, 'Profile_form.html', {'form': form})