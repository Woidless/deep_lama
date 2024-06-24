# home/views.py
from django.shortcuts import render

def home_view(request):
    context = {}
    return render(request, 'home/index.html', context)
