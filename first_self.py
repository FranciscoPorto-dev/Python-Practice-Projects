from datetime import datetime
from random import random
import requests
from requests.models import Response


def display_menu():
    current_time = datetime.now().time()
    hour = current_time.hour

    if 6 <= hour < 12:
        print('Good Morning and welcome to your to-do list :)')
    elif 12 <= hour < 18:
        print('Good Afternoon and welcome to your to-do list :)')
    elif 18 <= hour < 21:
        print('Good Evening and welcome to your to-do list :)')
    else:
        print('Good Night and welcome to your to-do list :)') #this line makes sense as you can't say 21 <= hour < 5 sicne the 21 is bigger than 5

    print('1. Add Task')
    print('2. See Tasks')
    print('3. Complete Task')
    print('4. Exit')



def add_task(to_do_list):
    task = (str(input('What would you like to add to your list?')))
    to_do_list.append(task)
    print('Task {} added successfully'.format(task))

def see_tasks(to_do_list):
    if not to_do_list:
        print('No tasks present in the to-do list')
    else:
        print('Tasks:')
    for index, task in enumerate(to_do_list, start = 1):
        print(f"{index}, {task}")

def complete_task(to_do_list):
    see_tasks(to_do_list)
    if to_do_list:
        try:
            index = int(input("Enter the number for the task you would like to remove: "))
            completed_task = to_do_list.pop(index-1)
            print('Task {} has been marked as completed.'.format(completed_task))
        except (ValueError, IndexError):
            print("Invalid list or index is not present on the list")

def main():
    to_do_list = []

    while True:
        display_menu()
        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            add_task(to_do_list)
        elif choice == '2':
            see_tasks(to_do_list)
        elif choice == '3':
            complete_task(to_do_list)
        elif choice == '4':
            print('Exiting to-do list goodbye :)')
            break
        else:
            print('Invalid input remember input must be in the range 1-4')

def weather_starter(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric' #this can be changed to imperial for farenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
           temperature = data['main']['temp']
           for condition in data['weather']:
               weather_description = condition['description']
               print(f"Weather in {city}: {weather_description}, Temperature: {temperature}°C")
        else:
           print(f"Error: {data['message']}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

api_key = 'b873c5438d01611faf27dc8ee7a345dd'
city_name = 'Panama'

if __name__ == "__main__":
    main()
    weather_starter(api_key, city_name)
