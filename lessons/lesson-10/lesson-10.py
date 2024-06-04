# # How many people are in space right now API
import pprint
import requests
#
# # Get request from the API
# endpoint = 'http://api.open-notify.org/astros.json'
# response = requests.get(endpoint)
# # Getting the status code from the API, 200 = ok
# print(response.status_code)
# data = response.json()
# # print(data)
#
# # pprint - prettier print
# pprint.pp(f"Total number of people in space: {data['number']}")
# #
# # # Iterate over each person in space and print their name
# # for person in data['people']:
# #     pprint.pp(person['name'])
#
# # Saving those names to a file
# with open('lesson-10-astronauts.txt', 'w') as text_file:
#     for person in data['people']:
#         text_file.write(person['name'] + "\n")

# Open weather API
api_key = 'd17387a96fc51cc65e1886351ade2b1a'
endpoint = 'https://api.openweathermap.org/data/2.5/weather'
pay_load = {
    'q': 'London, UK',
    'units': 'metric',
    'appid': api_key
}
response = requests.get(endpoint, params= pay_load)
data = response.json()
pprint.pp(data)

city_name = data['name']
temperature = data['main']['temp']
feels_like = data['main']['feels_like']

# Displaying the wind speed
wind_speed = data['wind']['speed']
print(f"The current wind speed in {city_name} is {wind_speed}")

# Displaying the humidity
humidity = data['main']['humidity']
print(f"The current humidity in {city_name} is {humidity}")

# Write the extracted information to a file
with open('lesson-10-weather.txt', 'w') as text_file:
    text_file.write(f"The temperature in {city_name} is {temperature}, but feels like {feels_like}\n")
    text_file.write(f"The current wind speed in {city_name} is {wind_speed}\n")
    text_file.write(f"The current humidity in {city_name} is {humidity}\n")

weather = data['weather'][0]['main'].lower()

print(f"The current weather in {city_name} is {weather}")

with open('lesson-10-weather.txt', 'a') as text_file:
    text_file.write(f"The current weather in {city_name} is {weather}")

