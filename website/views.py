from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from . import forms


def home(request):
    # check to see of logging in
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOU HAVE LOGGED IN!")
            return redirect(reverse('home'))
        else:
            messages.error(request, "THERE WAS AN ERROR THERE. PLEASE TRY AGAIN...!")
            return redirect(reverse('home'))
    else:
        return render(request, 'website/home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "YOU HAVE LOGGED OUT...!")
    return redirect(reverse('home'))


def register_user(request):
    register_form = forms.SignUpForm()
    context = {
        'register_form': register_form
    }
    return render(request, 'website/register.html', context)