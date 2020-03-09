# weatherAPI
Get Weather information

Prerequisites: - 
Should have install Python and Python IDE (PyCharm) to execute this program.
Steps: -
1. Get the code using git clone “https://github.com/shivamshukla-88/weatherAPI.git” or download the zip file from the provided git link.
2. After downloading, create new project in Python IDE.
3. Once you have created, open downloaded files into project.
4. You should see 4 files authDetails.py, openWeatherMap.py, weatherStack.py and weatherApiCall.py.
5. Create login in “http://api.weatherstack.com/” and generate "Access key". 
6. Create login in “http://api.openweathermap.org/” and generate "API key". We will use it to fetch the weather information later.
6. Pass your weather API "Access key" and "API key" into authDetails.py file.
7. Now run "weatherApiCall.py" file.
8. Copy URL from standard output located in the output terminal, and then open the URL into browser. It will show you a welcome message.
9. Now add extension to the URL "/v1/weather" (i.e. “http://localhost:8080/v1/weather”) , to get default city weather details (which is Melbourne). 
10. Also, you can add extension to the URL "/v1/weather?city=melbourne"(i.e. “http://localhost:8080/v1/weather?city=melbourne”) to get specific city weather details.
11. “http://api.weatherstack.com/” is a default weather API to get details. In case API is not up it will redirect to "http://api.openweathermap.org/".
12. You will see output as showcased below: 
   Output format: {"temperature_degrees":19,"wind_speed":24}
