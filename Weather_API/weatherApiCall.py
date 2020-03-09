from flask import Flask, request
import weatherStack
import openWeatherMap

def get_weather_info(city):

    #check return value and do failover.
    result = weatherStack.get_weather_info(city)
    if result == None or result.get('temperature_degrees') == None:
        result = openWeatherMap.get_weather_info(city)
        if result == None or result.get('temperature_degrees') == None:
            if openWeatherMap.last_timeStamp:
                result = openWeatherMap.last_result
            elif weatherStack.last_timeStamp:
                result = weatherStack.last_result
    return result

app = Flask(__name__)

#fatch details for /v1/weather url
@app.route('/v1/weather')
def weatherInfo():
    """ Weather web service """
    city = request.args.get("city", None) #Get city anme for argument
    return get_weather_info(city)

@app.route('/')
def weatherAPi():
    return '<h1>Welcome to weather app</h1>'

if __name__ == '__main__':
    app.run(host="localhost", port=8080, debug=False)
