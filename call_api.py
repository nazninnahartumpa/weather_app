import requests
from django.shortcuts import render
from requests.exceptions import HTTPError

from django.conf import settings


BASE_URL = settings.API_BASE_URL




# Start For GET All information for spacific doctor model
def get_weather_api(**args):
    """
    get the help post
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
