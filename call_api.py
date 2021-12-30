import requests
from django.shortcuts import render
from requests.exceptions import HTTPError

from django.conf import settings

# base url for the api url from setting file
BASE_URL = settings.API_BASE_URL




# Get weather info by city name
def get_weather_api(**args):
    """
    get weather data by city name
    """
    try:
        get_weather_api_url = BASE_URL + "/api/weather/"

        response = requests.post(
            get_weather_api_url,
            headers={
                "Content-Type": "application/json",
            },
            json={
                "city_name": args['city_name'],
            },
            verify=False
        )

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'get_weather_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'get_weather_api(): Other error occurred: {err}')
    else:
        print('get_weather_api(): Success!')

    return response


# Get day wise weather info
def get_daily_weather_api(**args):
    """
    get the daily weather data 
    """
    try:
        get_daily_weather_url = BASE_URL + "/api/daily_weather/"

        response = requests.post(
            get_daily_weather_url,
            headers={
                "Content-Type": "application/json",
            },
            json={
                "lat": args['lat'],
                "lon": args['lon'],
            },
            verify=False
        )

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'get_daily_weather_api(): HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'get_daily_weather_api(): Other error occurred: {err}')
    else:
        print('get_daily_weather_api(): Success!')

    return response
