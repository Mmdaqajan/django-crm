from django.shortcuts import render


def home(request):
    context = {

    }
    return render(request, 'website/home.html', context)
