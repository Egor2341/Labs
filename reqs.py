import json

import requests

API_KEY = '8494a8a0f63285886b520069bc729ace'
city_name = 'Moscow'
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={input('Hello, please write your city')}&units=metric&appid={API_KEY}").json()


print(f"""
{response["weather"][0]["main"]}, {response["weather"][0]["description"]}
temp = {response["main"]["temp"]}
feels_like = {response["main"]["feels_like"]}
temp_min = {response["main"]["temp_min"]}
temp_max = {response["main"]["temp_max"]}
pressure = {response["main"]["pressure"]}
humidity = {response["main"]["humidity"]}
wind: speed = {response["wind"]["speed"]}, deg = {response["wind"]["deg"]}""")
