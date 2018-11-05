from django.shortcuts import render
from places.models import HistoricPlaces


def home_page(request):
    historic_places = HistoricPlaces.objects.all()
    return render(request, 'places/home.html', {'historic_places': historic_places})
