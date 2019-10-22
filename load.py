import random
import string
from typingprint import *
import glob, os

def find_saves():
    list_file = []
    
    os.chdir(os.getcwd())
    os.chdir(os.getcwd() + "/Saves")
    for file in glob.glob("*.txt"):
        list_file.append(str(file))
    return(list_file)