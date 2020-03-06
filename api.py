import requests
import json
from datetime import datetime

def check_response(response):
    if response.status_code != 200:
        print('Error returned from API')
    else:
        print('Success')

# Find people currently in space.
response = requests.get("http://api.open-notify.org/astros.json")
check_response(response)
resp = response.json()
astronauts = [item['name'] for item in resp['people']]
print(astronauts)

# Input latitude and longitude and find times ISS will pass.
lat = input('Enter lat: ')
lon = input('Enter lon: ')

parameters = {"lat": lat, "lon": lon}
response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
check_response(response)
resp = response.json()
risetimes = [datetime.fromtimestamp(item['risetime']) for item in resp['response']]
print(risetimes[0])



