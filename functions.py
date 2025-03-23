# WeatherCLI
# Copyright (C) 2025 Lyxminx
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

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
    
    





