from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse
from .forms import SignUpForm, AddRecordForm
from .models import Record


def home(request):
    records = Record.objects.all()

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
        return render(request, 'website/home.html', {'records': records})


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


def customer_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        context = {
            'record': record
        }
        return render(request, 'website/records.html', context)
    else:
        messages.success(request, "YOU HAVE TO BE LOGGED IN.")
        return redirect(reverse('home'))


def delete_customer_record(request, pk):
    if request.user.is_authenticated:
        record = Record.objects.get(id=pk)
        record.delete()
        messages.success(request, "Record Deleted Successfully ... !!!")
        return redirect(reverse('home'))
    else:
        messages.success(request, "YOU HAVE TO BE LOGGED IN.")
        return redirect(reverse('home'))


def add_customer_record(request):
    add_customer_form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if add_customer_form.is_valid():
                add_record = add_customer_form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'website/add_record.html', {'add_customer_form': add_customer_form})
    else:
        messages.success(request, "You Must Be Logged In...")
        return redirect('home')


def edit_customer_record(request, pk):
    if request.user.is_authenticated:
        this_record = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance=this_record)
        if form.is_valid():
            form.save()
            messages.success(request, 'Record Has Been Updated!')
            return redirect('home')
        return render(request, 'website/edit_record.html', {'form': form, 'this_record': this_record})
    else:
        return redirect('home')
