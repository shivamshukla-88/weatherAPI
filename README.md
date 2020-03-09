# weatherAPI
Get Weather information

Prerequisites :- 

Should have install Python and should have install Python IDE (PyCharm).

Steps:-

1. Get the code using git clone https://github.com/shivamshukla-88/weatherAPI.git or download zip file.

2. After downloading create project in Python IDE, can download PyCharm IDE.

3. Once you have created, Open downloaded files into project.

4. You should see 4 files authDetails, openWeatherMap, weatherStack and weatherApiCall.

5. create login in http://api.weatherstack.com/ and generate "Access key". create login in http://api.openweathermap.org/ and generate "API key". We will use it to fetch the weather information later.

6. Pass you weather API "Access key" and "API key" into authDetails file.

7. Now run "weatherApiCall" file. 

8. Copy URL from std out and and open into browser. It will show welcome message.

9. Now add "/v1/weather" to url to get default city weather details(which is melbourne).

10. Or add "/v1/weather?city=melbourne" to URL to get specific city  weather details.

11. http://api.weatherstack.com/ is default weather API to get details. In case API is not up it will redirect to "http://api.openweathermap.org/".

12. You will see output in JSON format. Temprature in celsius and wind speed.
   Output format : {"temperature_degrees":19,"wind_speed":24}
