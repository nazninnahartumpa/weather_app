from django.urls import path
from . import views

urlpatterns = [
    
    path('weather/', views.weather_api, name="current_weather"),
    path('daily_weather/', views.daily_weather_api, name="daily_weather"),

]
