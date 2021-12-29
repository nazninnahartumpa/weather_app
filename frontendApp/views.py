from django.shortcuts import render
from call_api import get_weather_api, get_daily_weather_api

# Create your views here.


def home(request):

    context = {
                'weather_data': '',
                'day_wise_weather_data': '',
                'msg': ''
            }

    if request.POST:

        api_data = get_weather_api(city_name = request.POST.get('city_name'))
        # print('api_data',api_data)
        # print('api_data_lat',api_data.json()['lat'])
        # print('api_data_lon',api_data.json()['lon'])
        
        if api_data:

            day_wise_weather_data = get_daily_weather_api(
                                    lat = str(api_data.json()['lat']),
                                    lon = str(api_data.json()['lon'])
                                )
            print('day_wise_weather_data', day_wise_weather_data)
        else:
            day_wise_weather_data = ''

        if api_data.status_code == 200:

            context = {
                'weather_data': api_data.json(),
                'day_wise_weather_data' : day_wise_weather_data.json()
            }
            print('context', context)

            return render(request, 'index.html', context)
        else:
            context = {
                'weather_data': '',
                'day_wise_weather_data': '',
                'msg': 'Please enter a valid city !'
            }
            
            print('context', context)

            return render(request, 'index.html', context)

    else:
        return render(request, 'index.html', context)

