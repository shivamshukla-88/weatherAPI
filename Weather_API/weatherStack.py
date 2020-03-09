from authDetails import *
import requests
from datetime import datetime

last_result = None
last_timeStamp = None

#Get access key from authDetails
access_key = auth_details['access_key']

def get_weather_info(city=None):

    global last_result, last_timeStamp

    #Take default city Melbourne if city name is none
    if city is None:
        city = "Melbourne" # extracting city name from argument

    url = f'http://api.weatherstack.com/current?access_key={access_key}&query={city}'

    weather_status = requests.get(url) #calling API and storing api response

    #check weatherSatck API status is down or up
    if weather_status.status_code != 200:
        return None #if API is dwon return None
    else:
        weather_result = weather_status.json()
        #get weather details(wind and temp) from API reposnse json
        current_temperature = weather_result.get('current', {}).get('temperature')
        wind_speed = weather_result.get('current', {}).get('wind_speed')

        weather_info = {'wind_speed': wind_speed, 'temperature_degrees': current_temperature}

        #Store weather information and time stamp in last_result for further use
        last_result = weather_info
        last_timeStamp = datetime.now()
        return weather_info
