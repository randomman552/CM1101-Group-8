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
    
player = {
    "description": {

    },
    "memory": {
        "name": Get_Player_Name(),
        "age": Get_Player_Age()
    }
}

def Name_Shuffle(name):
    l = list(name)
    random.shuffle(l)
    result = ''.join(l)
    return result

#Settings for max carry weight and starting inventory
max_carry_weight = 2
inventory = []

# Start game at the reception
current_room = rooms["Bedroom"]
