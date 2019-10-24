import typingprint
import os
import datetime
import glob
import pickle
os.chdir(os.getcwd() + "/Saves")

def getfilename():
    """Generate a file name using current datetime """
    return(str(datetime.datetime.now().strftime("%d_%m_%Y_%H-%M-%S")))

def save(player, current_room, GETs, rooms):
    """Save data to a file."""
    fileName = getfilename() + ".sav"
    data_to_save = {
        "player": player,
        "room": current_room,
        "GETs": GETs,
        "rooms": rooms
    }

    if not os.path.exists(fileName):
        f = open(fileName,"ab")
        pickle.dump(data_to_save,f)
        f.close()

def load(filename):
    f = open(filename, "rb") 
    data_to_load = pickle.load(f)
    f.close()
    return data_to_load

def list_saves():
    list_file = []
    for file in glob.glob("*.sav"):
        list_file.append(str(file))
    return(list_file)
