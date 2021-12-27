import requests
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status





@api_view(["POST"])
def weather_api(request):

    city_name = request.data['city_name']

    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&units=imperial&appid=f958ea4aef8d5dcefb2b61cbfe63aa11'


        r = requests.get(url).json()
        # r = requests.get(url.format(city_name)).json()
        print('response', r)

        city_weather = {
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
       
        print('city_weather', city_weather)
        return Response(city_weather, status=status.HTTP_200_OK)

    except Exception as error:
        print("Error for getting weather info for given city", error)
        city_weather = {}
        return Response(city_weather, status=status.HTTP_404_NOT_FOUND)


