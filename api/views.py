import requests
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import status




# weather_api is an api to show current data like what is the temparature, sunset, sunrise etc...
@api_view(["POST"])
def weather_api(request):

    # get the city name and pass to the url
    city_name = request.data['city_name']

    try:
        url = 'http://api.openweathermap.org/data/2.5/weather?q='+ city_name +'&units=metric&appid=f958ea4aef8d5dcefb2b61cbfe63aa11'


        r = requests.get(url).json()

        # Make a dictionary of necessary information 
        city_weather = {
            'city' : r['name'],
            'temperature' : r['main']['temp'],
            'humidity' : r['main']['humidity'],
            'feels_like' : r['main']['feels_like'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
            'lat' : r['coord']['lat'],
            'lon' : r['coord']['lon'],
            'sunrise' : r['sys']['sunrise'],
            'sunset' : r['sys']['sunset'],

        }
       
        print(f'city_weather {city_weather}')
        return Response(city_weather, status=status.HTTP_200_OK)

    except Exception as error:
        print("Error for getting weather info for given city", error)
        city_weather = {}
        return Response(city_weather, status=status.HTTP_404_NOT_FOUND)



# daily_weather_api is a function to show detail weather info of next 8 days by passing lat and lon
@api_view(["POST"])
def daily_weather_api(request):

    # get lat, lon and pass to the url 
    lat = request.data['lat']
    lon = request.data['lon']

    try:
        url = 'https://api.openweathermap.org/data/2.5/onecall?lat=' + lat + '&lon=' + lon +'&units=metric&exclude=hourly, minutely&appid=f958ea4aef8d5dcefb2b61cbfe63aa11'


        r = requests.get(url).json()
        
        return Response(r, status=status.HTTP_200_OK)

    except Exception as error:
        print("Error for getting weather info for given city", error)
        r = {}
        return Response(r, status=status.HTTP_404_NOT_FOUND)


