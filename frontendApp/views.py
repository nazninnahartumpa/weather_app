from django.shortcuts import render
from call_api import get_weather_api

# Create your views here.


def home(request):

    context = {
                'weather_data': '',
                'msg': ''
            }

    if request.POST:
        api_data = get_weather_api(city_name = request.POST.get('city_name'))

        print('api_data',api_data)

        if api_data.status_code == 200:

            context = {
                'weather_data': api_data.json()
            }
            print('context', context)

            return render(request, 'index.html', context)
        else:
            context = {
                'weather_data': '',
                'msg': 'Please enter a valid city!!'
            }
            
            print('context', context)

            return render(request, 'index.html', context)

    else:
        return render(request, 'index.html', context)

