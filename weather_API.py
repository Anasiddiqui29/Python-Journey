#This is the weather app and data is requested from the website:"openweathermap" using API
#Please note that this is the prototype of how API works with python. To get the APIs , one must
#sign up to the relevant websites. All rights are reserved.

import requests

API_KEY = "Insert your API key here."
base_url = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_info(city):
    #create dictionary to tell the paramaters
    param = {
        "q":city,
        "appid":API_KEY,
        "units":"metrics"
    }

    response = requests.get(base_url , params=param)

    if response.status_code == 200:
        #this means that website is responding
        weather_data = response.json() #This fucntion converts the data to relevant pyhton library
        temp = weather_data["main"]["temp"]
        desc = weather_data["weather"][0]["description"]
        print("Weather in city {}".format(city))
        print("Temperature: {}".format(temp))
        print("Condition: {}".format(desc))
    else:
        print("City not found or API error")


print("Welcome to the WEATHER app.")
city_name = input("Enter a city name to get started: ")
get_weather_info(city_name)