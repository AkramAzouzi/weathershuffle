import datetime
from django.shortcuts import render
import geocoder as geocoder
import requests
from django.http import HttpResponse

from meteo.models import Worldcities

# Create your views here.


def temp_here(request):
    location = geocoder.ip("me").latlng
    city = geocoder.ip("me").city
    temp = get_temp(location)
    context = {"city": city, "temp": temp}
    return render(request, "meteo/index.html", context)


def get_temp(location):
    endpoint = "https://api.open-meteo.com/v1/forecast"
    api_request = f"{endpoint}?latitude={location[0]}&longitude={location[1]}&hourly=temperature_2m"
    now = datetime.datetime.now()
    hour = now.hour
    meteo_data = requests.get(api_request).json()
    temp = meteo_data["hourly"]["temperature_2m"][hour]
    return temp


def temp_somewhere(request):
    random_item = Worldcities.objects.all().order_by("?").first()
    city = random_item.city
    location = [random_item.lat, random_item.lng]
    temp = get_temp(location)
    context = {"city": city, "temp": temp}
    return render(request, "meteo/index.html", context)
