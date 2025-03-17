# Imports
import requests
from os import system, name
from dotenv import load_dotenv
import os

#Parts of this function is borrowed from William James Dominic Liwanag Shorter
# Gets the weather info of a city based on the url provided.
def get_Weather(url):
    # Gets the useragent from .env
    load_dotenv()
    user_agent = os.getenv("USER_AGENT")
    headers = {
        "User-Agent": user_agent
    }

    # Gets the weather info based on url, and adds the User-Agent for identification
    response = requests.get(url, headers=headers)

    # Checks if we get a valid reponse
    if response.status_code == 200:
        try:
            # Gets all weatherdata in a json format
            data = response.json()
            details = data['properties']['timeseries'][0]['data']['instant']['details']
            # Sets the temperature and precipitation to either reflect the current weather conditions or sets it to None and 0 if the response doesn't work
            airtemp = details.get('air_temperature', None)
            precipitation = details.get('precipitation_amount', 0) 
            
        except (KeyError, IndexError):
            airtemp = None
            precipitation = 0
    else:
        airtemp = None
        precipitation = 0
    # Returns a dictionary with the weather conditions
    return {"airtemp":airtemp,"precipitation":precipitation}

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    
    





