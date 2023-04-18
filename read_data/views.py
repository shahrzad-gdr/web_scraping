from django.shortcuts import render


def home(request):
    return render(request, 'read_data/index.html')