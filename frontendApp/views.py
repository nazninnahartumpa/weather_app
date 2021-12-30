from django.shortcuts import render

# Calling function from call_api.py file
from call_api import get_weather_api, get_daily_weather_api



# This is home function for selecting city name and show the daily results
def home(request):

    # Initialize the variable as empty
    context = {
                'weather_data': '',
                'day_wise_weather_data': '',
                'msg': ''
            }

    if request.POST:
        # Getting city name from the search form....
        api_data = get_weather_api(city_name = request.POST.get('city_name'))
        
        if api_data:
            # if city is searched then lat and lon value pass to the get_daily_weather_api
            day_wise_weather_data = get_daily_weather_api(
                                    lat = str(api_data.json()['lat']),
                                    lon = str(api_data.json()['lon'])
                                )
            print(f'day_wise_weather_data {day_wise_weather_data}')
        else:
            day_wise_weather_data = ''

        # If response is success then data pass to the html page  
        if api_data.status_code == 200:

            # here weather_data refers to the current data and day_wise_weather_data refers to the next 8 days weather data
            context = {
                'weather_data': api_data.json(),
                'day_wise_weather_data' : day_wise_weather_data.json()
            }

            return render(request, 'index.html', context)
        
        # If response is not success then pass the empty dict and message
        else:
            context = {
                'weather_data': '',
                'day_wise_weather_data': '',
                'msg': 'Please enter a valid city !'
            }
        
            return render(request, 'index.html', context)

    else:
        return render(request, 'index.html', context)
    
    


