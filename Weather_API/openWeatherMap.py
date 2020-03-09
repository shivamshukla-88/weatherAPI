from authDetails import *
import requests
from datetime import datetime

# extracting api_key and access key
api_key = auth_details['api_key']

last_result = None
last_timeStamp = None

def get_weather_info(city=None):
    
    global last_result, last_timeStamp

    if city is None:
        city = "Melbourne"  # extracting city name from argument

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city},AU&appid={api_key}'
    weather_status = requests.get(url)  # calling API and storing api response

    if weather_status.status_code != 200:
        return None
    else:
        # if first API call is success then using JSON
        weather_result = weather_status.json()

        # get weather details(wind and temp) from API reposnse json
        wind_speed = weather_result.get('wind', {}).get('speed')
        current_temperature = weather_result.get('main', {}).get('temp')

        # converting temprature it into Celsius
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        weather_info = {'wind_speed': wind_speed, 'temperature_degrees': current_temperature_celsius}

        # Store weather information and time stamp in last_result for further use
        last_result = weather_info
        last_timeStamp = datetime.now()
        return weather_info
