from django.shortcuts import render
from .models import city_db


def city_detail(request, pk):
    name = city_db[pk]['name']
    description = city_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'city/city-detail.html', context)
