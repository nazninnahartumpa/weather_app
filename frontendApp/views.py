from django.shortcuts import render
from call_api import get_weather_api

# Create your views here.


def home(request):

    api_data = get_weather_api()

    print('api_data',api_data)

    context = {
        'weather_data': api_data.json()
    }
    print('context', context)

    return render(request, 'index.html', context)

