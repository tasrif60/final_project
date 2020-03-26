from django.shortcuts import render, redirect, get_object_or_404
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

########## CRUD operation of Profile ############


def load_profile(request):
    all_profile = Profile.objects.all()
    datadictionary = {

        'object': all_profile

    }
    return render(request, 'profile_list.html', datadictionary)

def create_profile(request, *args, **kwargs):
    if request.method == 'POST':
        prof_form = ProfileForm(request.POST)
        if prof_form.is_valid():
            prof_form.save(commit=True)
            return redirect('profile_list.html')

    form = ProfileForm()
    return render(request, 'Profile_form.html', {'form': form})


def update_profile(request, pk):
    profile_details = get_object_or_404(Profile, pk=pk)
    form = ProfileForm(request.POST or None, instance=profile_details)
    if form.is_valid():
        form.save()
        return redirect('profile_list.html')
    form=ProfileForm()
    return render(request, ProfileForm, {'form': form})