# Run the project:
To run the project just clone from the master branch and run the command: docker-compose up --build
Then go to the http://127.0.0.1:8000/ and can see the home page of the project.
Then add a city from the search field and can see the weather results as current result and next 8 days weather result.
By clicking the text English can see English translation and Bangoli is the default laguage. Here I am using i18 for the internationalization.
# About project:
By API from the manue you can go to the api.
`api/weather/` is the url for current weather and `api/daily_weather/` is the url for next 8 days weather data.
You can post to `api/weather/` url as `{"city_name":"dhaka"}` this way.
And can post to the url `api/daily_weather/` `{"lat": "city_lat_data", "lon": "city_lon_data"}` this way.
# If I have more time
If I have more time I will implement the Cached api results and type hinting.
Here I actually focus on backend part because I am interested in backend part more then frontend. I can work as full stack developer but I am more interested in backend part.
