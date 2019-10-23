from map import *
from typingprint import *
import os
import datetime
import glob

def getfilename():
    """Generate a file name using current datetime """
    return(str(datetime.datetime.now().strftime("%d_%m_%Y_%H-%M-%S")))

def save_data(player, current_room, GETs):
    fileName = "Saves/" + getfilename() + ".txt"
    if not os.path.exists(fileName):
        try:
            f = open(fileName,"w+")
            f.write(str(player) + "\n")
            f.write(str(current_room["name"]) + "\n")
            f.write(str(GETs) + "\n")
            f.write(str(items_in_rooms()))

            slow_print("Game Saved!!!")
            return()
        except:
            slow_print("There was an error saving your game, please try again...")
    slow_print("There was an error saving your game, please try again...")

def items_in_rooms():
    room_items = {}
    for room in rooms:
        room_items[room] = rooms[room]["items"]["id"]

    return(room_items)

def find_saves():
    list_file = []
    
    os.chdir(os.getcwd())
    os.chdir(os.getcwd() + "/Saves")
    for file in glob.glob("*.txt"):
        list_file.append(str(file))
    return(list_file)