import requests
import json
from datetime import datetime
import os
import time

def clear():
    os.system('clear')

clear()

def check_response(response):
    if response.status_code != 200:
        print('Error returned from API')
    else:
        print('Success')

def astronauts():
    # Find people currently in space.
    response = requests.get("http://api.open-notify.org/astros.json")
    check_response(response)
    resp = response.json()
    astronauts = [item['name'] for item in resp['people']]
    print(astronauts)
    time.sleep(2)
    clear()

def location():
    # Input latitude and longitude and find times ISS will pass.
    lat = input('Enter lat: ')
    lon = input('Enter lon: ')

    parameters = {"lat": lat, "lon": lon}
    response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
    check_response(response)
    resp = response.json()
    risetimes = [datetime.fromtimestamp(item['risetime']) for item in resp['response']]
    print(risetimes[0])
    time.sleep(2)
    clear()


selections = {
        "1": astronauts,
        "2": location,
        }

for k, v in selections.items():
    print(f'{k}-------------------{v.__name__}')

select = input("Enter selection: ")

selections[select]()

# oop way

class Astronauts:
    def get_names(self):
        # Find people currently in space.
        response = requests.get("http://api.open-notify.org/astros.json")
        check_response(response)
        resp = response.json()
        astronauts = [item['name'] for item in resp['people']]
        print(astronauts)
        time.sleep(2)
        clear()

funcs = Astronauts()

selections = {
        "1": "get_names",
        }

for k, v in selections.items():
    print(f'{k}-------------------{v}')

while True:
    user_input = input()
    getattr(funcs, selections[user_input])()
