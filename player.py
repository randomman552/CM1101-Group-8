from items import *
from map import rooms
from gameparser import *
import random
import os

def Get_Player_Name():
    """Used to get players name when game starts up"""
    print("Please enter your name: ")
    return str(input())
    
def Get_Player_Age():
    """Used to get players age when game starts up"""
    print("Please enter your age: ")
    try:
        return int(input())
    except ValueError:
        #If the user enters a value that is not a number, quit the game.
        print("Thats not a number!")
        os.system("pause")
        quit()
        
player = {}
playerdefault = {
    "stage": 0,
    "psychosis meter": 0,
    "inventory": [],
    "description": {

    },
    "memory": {
        "name": "Bob",
        "age": "3000",
        "password": [] #Placeholder, for use in password puzzle?
    }
}

def Name_Shuffle(name):
    l = list(name)
    random.shuffle(l)
    result = ''.join(l)
    return result


# Start game in the bedroom
current_room = rooms["Bedroom"]
previous_room = ""
