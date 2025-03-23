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
from functions import *
from possistions import *
import readchar
import sys

def selectCity():
    # Gets all cities from the dictionary in the possistions.py
    from possistions import cities
    # Gets city names
    cities = list(cities.keys())
    # Adds exit option
    cities.append('Exit')
    # For checking the selected city
    selected = 0
    # To enable and disable searchmode
    search_mode = False 

    while True:
        # Just clears the screen
        clear()
        print('Select a city or hit "/" to search:')
        # Prints all cities and adds indentation before the name. Also adds an arrow to show which option is selected.
        for i, city in enumerate(cities):
            prefix = "> " if i == selected else "  "
            print(prefix + city)
        # Starts listening for keypresses
        key = readchar.readkey()
        # Moves up if the up arrow or k is pressed
        if key == readchar.key.UP or key == 'k' and selected > 0:
            selected -= 1
        # Moves down if the down arrow or j is pressed
        elif key == readchar.key.DOWN or key == 'j' and selected < len(cities) - 1:
            selected += 1
        # selects option if Enter is pressed
        elif key == readchar.key.ENTER:
            clear()
            # As long as it is not exit return the option that is selected
            if cities[selected] != 'Exit':
                return cities[selected]
            # If it is exit, stop the program
            else:
                sys.exit()
        # Checks if / is pressed
        elif key == "/":
            # Enables searchmode
            search_mode = True
            search_query = ""
            all_cities = cities 
            filtered_cities = all_cities 

            while search_mode:
                clear()
                print(f"Search mode ON | Query: {search_query}")
                
                #Prints all cities that match the query with indentation
                for city in filtered_cities:
                    print("  " + city)

                key = readchar.readkey()
                # If esc is pressed, exit search mode
                if key == readchar.key.ESC:  
                    search_mode = False
                    filtered_cities = all_cities  
                    search_query = ""
                # Removes the last letter as long as the query is more than 0 characters long
                elif key == readchar.key.BACKSPACE and len(search_query) > 0:  
                    search_query = search_query[:-1]
                # If enter is pressed it returns all cities that match the query
                elif key == readchar.key.ENTER:  
                    cities = filtered_cities
                    search_mode = False
                # Any other key will be added to the query 
                else:
                    search_query += key
                # Makes an array with all cities that match the query
                filtered_cities = [city for city in all_cities if search_query.lower() in city.lower()]
                # Adds Exit if it isn't in the filtered list.
                if "Exit" not in filtered_cities:
                    filtered_cities.append("Exit")
                
# Runs the menu and saves the selected city
selected_city = selectCity()

# Gets the airtemperature of the selected city
airtemp = get_Weather(cities[selected_city])['airtemp']
# Gets the amount of precipitation (rain) of the selected city
precipitation = get_Weather(cities[selected_city])['precipitation']

# outputs based on temperature and precipitation
if airtemp is None:
    print("Cannot fetch weatherdata, stick your head out of the window or smth IDK...")

elif airtemp > 15 and precipitation == 0:
    print('It is warm outside, go touch some grass kid!')
    print(f'The temperature is {airtemp}°C, and it is not raining.')

elif airtemp <= 15 and precipitation == 0:
    print('It is cold out, so maybe wear a jacket. Go touch some grass kiddo!')
    print(f'The temperature is {airtemp}°C, and it is not raining.')

elif precipitation > 0:
    print("It's raining, maybe stay inside today!")
    print(f'The temperature is {airtemp}°C')
print('-----------------')
input('Hit ENTER to exit')
clear()