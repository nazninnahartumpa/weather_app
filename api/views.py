import requests
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response




@api_view(["GET"])
def weather_api(request):

    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q=Dhaka&units=imperial&appid=f958ea4aef8d5dcefb2b61cbfe63aa11'

        r = requests.get(url).json()
        print('response', r)

        city_weather = {
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }
       
        print('city_weather', city_weather)
        return Response(city_weather)

    except Exception as error:
        print("Error for getting weather info for given city", error)
        return Response(data={"success": False, "error": error})


