from possistions import cities
import requests
from os import system, name
from dotenv import load_dotenv
import os

def get_Weather(url):
    
    load_dotenv()

    # Retrieve the user-agent from the environment variable
    user_agent = os.getenv("USER_AGENT")

    # Use the user-agent in your headers
    headers = {
        "User-Agent": user_agent
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            data = response.json()
            details = data['properties']['timeseries'][0]['data']['instant']['details']
            
            airtemp = details.get('air_temperature', None)
            precipitation = details.get('precipitation_amount', 0)  # Defaults to 0 if missing
            
        except (KeyError, IndexError):
            airtemp = None
            precipitation = 0
    else:
        airtemp = None
        precipitation = 0
    return {"airtemp":airtemp,"precipitation":precipitation}


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
    





