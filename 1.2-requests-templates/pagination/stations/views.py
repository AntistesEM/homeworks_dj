import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from pagination import settings


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    bus_stations = []
    with open(settings.BUS_STATION_CSV, newline='', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            stations = {}
            stations['Name'] = row['Name']
            stations['Street'] = row['Street']
            stations['District'] = row['District']
            bus_stations.append(stations)
        paginator = Paginator(bus_stations, 10)
        page_num = int(request.GET.get('page', 1))
        page = paginator.get_page(page_num)
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': page,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
