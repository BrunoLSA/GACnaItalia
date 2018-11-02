from django.conf import settings
from django.shortcuts import render


def home_page(request):
    context = {
        'api_key': settings.GOOGLE_MAPS_API_KEY
    }
    return render(request, 'places/home.html', context)
