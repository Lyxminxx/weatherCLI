from functions import *
from possistions import *
import readchar
import sys

def selectCity():
    from possistions import cities
    cities = list(cities.keys())
    cities.append('Exit')
    selected = 0
    search_mode = False 
    while True:
        clear()  # Assuming you have a 'clear' function that clears the screen
        print('Select a city or hit "/" to search:')
        for i, city in enumerate(cities):
            prefix = "> " if i == selected else "  "
            print(prefix + city)

        key = readchar.readkey()
        if key == readchar.key.UP or key == 'k' and selected > 0:
            selected -= 1
        elif key == readchar.key.DOWN or key == 'j' and selected < len(cities) - 1:
            selected += 1
        elif key == readchar.key.ENTER:
            clear()
            if cities[selected] != 'Exit':
                return cities[selected]
            else:
                sys.exit()
        elif key == "/":
            search_mode = True
            search_query = ""
            all_cities = cities  # Keep original city list
            filtered_cities = all_cities  # Start with all cities

            while search_mode:
                clear()
                print(f"Search mode ON | Query: {search_query}")
                
                # Show filtered results
                for city in filtered_cities:
                    print("  " + city)

                key = readchar.readkey()

                if key == readchar.key.ESC:  # Exit search mode
                    search_mode = False
                    filtered_cities = all_cities  # Reset filter
                    search_query = ""

                elif key == readchar.key.BACKSPACE and len(search_query) > 0:  # Delete last character
                    search_query = search_query[:-1]

                elif key == readchar.key.ENTER:  # Exit search mode
                    cities = filtered_cities
                    search_mode = False
                else:
                    search_query += key  # Append new character

                # Update filtered cities based on search query
                filtered_cities = [city for city in all_cities if search_query.lower() in city.lower()]
                filtered_cities.append("Exit")
                
                
                
# Call the function to display and select a city
selected_city = selectCity()

airtemp = get_Weather(cities[selected_city])['airtemp']
precipitation = get_Weather(cities[selected_city])['precipitation']
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