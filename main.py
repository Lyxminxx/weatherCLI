from functions import *
from possistions import *
import readchar
import sys

def selectCity():
    from possistions import cities
    cities = list(cities.keys())
    cities.append('Exit')
    selected = 0
    while True:
        clear()  # Assuming you have a 'clear' function that clears the screen
        print("Select a city:")
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