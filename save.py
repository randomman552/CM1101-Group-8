
from typingprint import *
import os
import datetime
import glob

def getfilename():
    """Generate a file name using current datetime """
    return(str(datetime.datetime.now().strftime("%d_%m_%Y_%H-%M-%S")))

def save_data(player):
    fileName = "Saves/" + getfilename() + ".txt"
    if not os.path.exists(fileName):
        try:
            f = open(fileName,"w+")
            f.write(str(player))
            slow_print("Game Saved!!!")
            return()
        except:
            slow_print("There was an error saving your game, please try again...")
    slow_print("There was an error saving your game, please try again...")

def find_saves():
    list_file = []
    
    os.chdir(os.getcwd())
    os.chdir(os.getcwd() + "/Saves")
    for file in glob.glob("*.txt"):
        list_file.append(str(file))
    return(list_file)