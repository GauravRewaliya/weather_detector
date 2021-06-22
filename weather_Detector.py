
import requests

from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'  ##like username,pass
location = input("Enter the city name: ")   ##ask to enter loc 

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
r  = requests.get(complete_api_link)   #send request   ##request pointer 

api_data = r.json()  ## read data " as json 


#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
 
with open("weather_result.txt", "w") as f:
    f.write("-------------------------------------------------------------\n"
             +"Weather Stats for - {}  || {}\n".format(location.upper(), date_time) 
             + "-------------------------------------------------------------\n"

            + "Current temperature is: {:.2f} deg C\n".format(temp_city) 
           +"Current weather desc  : {}\n".format(weather_desc) 
             +"Current Humidity      : {}".format(hmdt) + '%'
           + "\nCurrent wind speed    :{}".format(wind_spd) +'kmph'
           ) 