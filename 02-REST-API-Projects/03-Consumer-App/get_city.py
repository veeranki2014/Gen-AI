import requests

city = "Hyderabad"

api_url = "https://geocoding-api.open-meteo.com/v1/search"

params = {
    "name": "Hyderabad",
    "country": "India",
    "count" : 1
}

response = requests.get(api_url,params)
print(response.text)


###--------------------------------------------------####

latitude = 17.38405
longitude = 78.45636

url = "https://api.open.meteo.com/v1/forecast"
params = {
    latitude : latitude,
    longitude : longitude,
    "current" : "temperature_2m, relative_humidity_2m, air_temperature_2m",
    "timezone": "auto"
}

response = requests.get(url,params)
print(response.text)






