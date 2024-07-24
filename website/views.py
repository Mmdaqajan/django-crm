from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import SignUpForm


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
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'website/register.html', {'register_form': form})

    return render(request, 'website/register.html', {'register_form': form})
