from map import *
from items import items
from gameparser import *
import os
import mainmenu
import sound
os.system("mode con: cols="+ str(mainmenu.maxwidth) + " lines="+ str(mainmenu.maxheight))
from player import *
import typingprint
import pygame
from pygame import mixer
import save

#Initialise inventory as a global variable
inventory = player["inventory"]
#Initialise pygame and and its mixer in the main thread. 
#Pygame is used in this project, but is only used to play sound
pygame.init()
pygame.mixer.init()
#Start background music, can be stopped at any point by calling BG_Music(False)
sound.BG_Music()

#type_print is a global variable that is used to define whether printing is instant or not.
#for example, typingprint.slow_type("Hello", type_print) would print instantly if print_type was true, and type it if false.
#this is used so that if the user has not changed room, the text is not typed out again.
type_print = True

def generate_GETs_items(items):
    """This function goes through all items inputted into it, 
    and finds what event triggers are present in all of them.
    These are then added to the GETs dict"""
    #Set output to an empty dict to start
    output = {}
    #For each item in the game
    for item in items:
        #Switch string for actual itme dict
        item = items[item]
        #If item is usable
        if "use" in item:
            #If it has conditions
            if "conditions" in item["use"]:
                #For each condition
                for condition in item["use"]["conditions"]:
                    #Check that the condition is not an item requirement
                    if not condition == "items":
                        #Add the condition to the output, ignore any that have already been added
                        if not condition in output:
                            #Detect the type of variable assigned to the GET, and give each GET a default value of that type
                            item_type = type(item["use"]["conditions"][condition])
                            if  item_type == bool:
                                default_value = False
                            elif item_type == str:
                                default_value = ""
                            elif item_type == int or item_type == float:
                                default_value = 0
                            output.update({condition: default_value})
    return output

def generate_GETs_rooms(rooms):
    output = {}
    #For each item in the game
    for room in rooms:
        #Switch string for actual itme dict
        room = rooms[room]
        #If it has conditions
        if "conditions" in room:
            #For each condition
            for condition in room["conditions"]:
                #Add the condition to the output, ignore any that have already been added
                if not condition in output:
                    #Detect the type of variable assigned to the GET, and give each GET a default value of that type
                    item_type = type(room["conditions"][condition])
                    if  item_type == bool:
                        default_value = False
                    elif item_type == str:
                        default_value = ""
                    elif item_type == int or item_type == float:
                        default_value = 0
                    output.update({condition: default_value})
    return output

#Global event triggers dictionary
#This is generated when the game starts, so any changes in items or rooms are reflected here
def generate_all_GETs():
    output = generate_GETs_items(items)
    output.update(generate_GETs_rooms(rooms))
    return output

GETs = generate_all_GETs()

class ANSIstyles:
    #This class can be used to format text by printing it before the text you want to format.
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:
    """

    Output = ""
    for item in items:
        Output = Output + item["name"]
        if not (item == items[len(items) - 1]):
            Output = Output + ", "
    return Output

def return_room_items(room):
    """This function takes a room as an input and nicely displays the items in the room in a string.
    The string is then returned to be used elsewhere
    """

    items_in_room = list_of_items(room["items"])
    if not(items_in_room == ''):
        return "There is " + items_in_room + " here.\n"
    else:
        return "There are no items here.\n"

def return_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely in a string.
    It then returns this string to be used elsewhere.
    """
    
    printstr = "You don't have any items.\n"
    items_in_inven = list_of_items(items)
    #If the player has items, return a list of them. Otherwise return the error string
    if not (items_in_inven == ''):
        printstr = "You have " + items_in_inven + ".\n"
    return printstr


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this)."""

    #Display room name in BOLD, then print description
    printstr = "\n"+ ANSIstyles.BOLD + room["name"].upper() + ANSIstyles.END + "\n\n" + room["description"] + ".\n"
    typingprint.slow_print(printstr,type_print)
    #Print items in room
    typingprint.slow_print(return_room_items(room),type_print)


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:"""
    #Work out what the next room is
    next_room = exit_leads_to(exits, chosen_exit)
    #If the exit exists
    if not next_room == None:
        #Check the conditions of the room
        if check_item_conditions(next_room):
            #If the conditions are met, return the corresponding exit
            return chosen_exit in exits
    #If none of the conditions above are met, return None
    return None
    


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if is_valid_exit(current_room["exits"],direction):
        current_room = move(current_room["exits"],direction)
        printstr = "Moving to " + current_room["name"]
    else:
        printstr = ANSIstyles.RED + "You cannot go there." + ANSIstyles.END
    return printstr

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    #Used to store the finally printed value.
    printstr = ANSIstyles.RED + "You cannot take that." + ANSIstyles.END
    #Check if the item exists.
    if item_id in items:
        #Switch string input for valid item id.
        item_id = items[item_id]
        #Check if the item can be taken.
        if item_id["take"] == True:
            #Check if the item is in the current room.
            if item_id in current_room["items"]:
                #Remove it from the room and put it in the players inventory.
                inventory.append(item_id)
                current_room["items"].remove(item_id)
                printstr = "Picked up " + ANSIstyles.BLUE +  item_id["name"] + ANSIstyles.END + "."
                #Play pickup sound
                sound.play_pickup_sound()
    #Will print the take message, unless the item has not be picked up.
    return printstr

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    #Printstr used to hold the final result of the function
    printstr = ANSIstyles.RED + "You cannot drop that" + ANSIstyles.END
    #If item exists
    if item_id in items:
        item_id = items[item_id]
        #If item in inventory
        if item_id in inventory:
            #Remove the item from your inventory and return a string to relay the information
            inventory.remove(item_id)
            current_room["items"].append(item_id)
            printstr = "Dropped " + ANSIstyles.BLUE + item_id["name"] + ANSIstyles.END + "."
            sound.play_drop_sound()
    return printstr

def deep_inspect(item_id):
    """This function provides further information about an item if certain items are present in the players inventory
    and if it has an inspect atribute."""
    #If the magnifying glass has been collected or used.
    if item_magnifying_glass in inventory:
        #If the item has an inspection atribute.
        if "inspection" in item_id:
            #return in inspection string
            return("Looking with the magnifying glass:\n" + item_id["inspection"])
        print("You cannot deep inspect without a magnifying glass.")
    #Return an empty string to prevent program crashes
    return ""

def execute_inspect(item_id):
    """This function takes an item_id as an argument, then prints the description of that item.
    If the item does not exist then it prints "That item does not exist".
    """
    #Printstr used to hold the final result of the function
    printstr = ANSIstyles.RED + "You cannot inspect that." + ANSIstyles.END
    #If the item exists
    if item_id in items:
        #Retrieve actual itme id from items list
        item_id = items[item_id]
        #If item is in inventory or in the current room
        if item_id in inventory or item_id in current_room["items"]:
            #Print item description
            printstr = item_id["id"] + ":\n" + item_id["description"]
            printstr += "\n" + deep_inspect(item_id)
            sound.play_inspect_sound()
    return printstr

def check_item_conditions(item_id):
    """Checks if item requirements are met"""
    output = True
    if "id" in item_id:
        if "conditions" in item_id["use"]:
            for condition in item_id["use"]["conditions"]:
                if condition == "items":
                    for item in item_id["use"]["conditions"]["items"]:
                        if not ((item in inventory) or (item in current_room["items"])):
                            return False
                elif not GETs[condition] == item_id["use"]["conditions"][condition]:
                    return False
    elif item_id["name"] in rooms:
        if "conditions" in item_id:
            for condition in item_id["conditions"]:
                if condition == "items":
                    for item in item_id["conditions"]["items"]:
                        if not ((item in inventory) or (item in current_room["items"])):
                            return False
                elif not GETs[condition] == item_id["conditions"][condition]:
                    return False
    return output

def apply_item_effects(item_id):
    """This function takes an item id as an argument, and changes values in the program depending on its effects."""
    global player
    global GETs
    use = item_id["use"]
    if "stage effect" in use:
        player["stage"] = use["stage effect"]
    if "sanity effect" in use:
        player["sanity"] = player ["sanity"] + use["sanity effect"]
    if "items" in use:
        for item in use["items"]:
            inventory.append(item)
    if "GETs effect" in use:
        for effect in use["GETs effect"]:
            GETs[effect] = use["GETs effect"][effect]
    sound.play_use_sound()

def execute_use(item_id):
    """Allows player to use an item, takes item_id as an argument"""
    #If item fails all of the checks, this string will be printed.
    printstr = ANSIstyles.RED + "You cannot use that." + ANSIstyles.END
    #Check if the item exists.
    if item_id in items:
        item_id = items[item_id]
        #Check if its in the players inventory.
        if (item_id in inventory) or (item_id in current_room["items"]):
            #Check if it's usable.
            if "use" in item_id:
                #Check if item requirements are met
                if(check_item_conditions(item_id)):
                    #Open unique prompts
                    if item_id["id"] == "mirror":
                        print_mirror_menu()
                    elif item_id["id"] == "computer":
                        password_prompt()
                    elif item_id["id"] == "picture":
                        print_picture_info()
                    #Print the use text, if it has any
                    if "text" in item_id["use"]:
                        printstr = item_id["id"] + ":\n" + item_id["use"]["text"]
                    apply_item_effects(item_id)
                    #If the item contains a function, call it.
                    if "function" in item_id["use"]:
                        item_id["use"]["function"]()
                    #If the item had item requirements, remove those items from the inventory.
                    if "conditions" in item_id["use"]:
                        if "items" in item_id["use"]["conditions"]:
                            for item in item_id["use"]["conditions"]["items"]:
                                if item in inventory:
                                    inventory.remove(item)
                                else:
                                    current_room["items"].remove(item)
                    #If the item needs to be removed after use, remove it from inventory or room.
                    if item_id["use"]["remove after use"]:
                        if item_id in inventory:
                            inventory.remove(item_id)
                        elif item_id in current_room["items"]:
                            current_room["items"].remove(item_id)
    return printstr

def print_picture_info():
    print("Is that me?... in the scarf?... " + player["reality"]["hair_length"] + ", " + player["reality"]["hair_colour"] + " hair.")

def print_mirror_menu():
    global player
    Finished = False
    while Finished != True:
        print("You look into the mirror. It's magical presence enraptures you...")
        print("What would you like to change?")
        print(" [1] Height")
        print(" [2] Eye Colour")
        print(" [3] Hair Colour")
        print(" [4] Hair Length")
        print(" [5] Gender")
        print(" [6] Name")
        print("")
        print(" [7] Show Appearance")
        print(" [8] Exit")
        i = str(input())
        s = ""
        if os.name == 'nt':
            os.system("cls")
        else:
            os.system("clear")

        for ch in i:
            if ch.isdigit() == True:
                s = s + ch
        if s == "1":
            print_list(player["options"]["height"], "height")
            Finished = check_appearance()

        elif s == "2":
            print_list(player["options"]["eye_colour"], "eye_colour")
            Finished = check_appearance()
        elif s == "3":
            print_list(player["options"]["hair_colour"], "hair_colour")
            Finished = check_appearance()
        elif s == "4":
            print_list(player["options"]["hair_length"], "hair_length")
            Finished = check_appearance()
        elif s == "5":
            print_list(player["options"]["gender"], "gender")
            Finished = check_appearance()
        elif s == "6":
            print("Please enter your name: ")
            name = str(input())
            player["description"]["name"] = name
            Finished = check_appearance()
            
        elif s == "7":
            print_appearance()
        elif s == "8":
            break
        #After the item has finished it's task, remove it.
        if Finished == True:
            rooms["Bathroom"]["items"].remove(item_mirror)
        
def print_appearance():
    global player
    print("Your name is " + player["description"]["name"] + " and you are a " + player["description"]["height"] +  " tall " + player["description"]["gender"] + ". You have "
    + player["description"]["hair_length"] + " " + player["description"]["hair_colour"] + " hair with " + player["description"]["eye_colour"] + " eyes.")
    
def check_appearance():
    global player
    counter = 0
    
    if player["description"]["name"].lower() == player["reality"]["name"].lower():
        counter += 1
    if player["description"]["height"] == player["reality"]["height"]:
        counter += 1
    if player["description"]["hair_colour"] == player["reality"]["hair_colour"]:
        counter += 1
    if player["description"]["hair_length"] == player["reality"]["hair_length"]:
        counter += 1
    if player["description"]["eye_colour"] == player["reality"]["eye_colour"]:
        counter += 1
    if player["description"]["gender"] == player["reality"]["gender"]:
        counter += 1    
    if counter == 6:
        typingprint.slow_print("Congratulations you know who you are. \nYou go the office key!!!", True)
        inventory.append(item_key)
        return True
    
    return False

def print_list(lists, command):
    global player
    counter = len(lists)
    print("Pick a value")
    for line in lists:
        print(" [" + str(lists.index(line) + 1) + "] " + line)

    i = str(input())
    s = ""
    for ch in i:
        if ch.isdigit() == True:
            s = s + ch

    player["description"][command] = lists[int(s)-1]
    print("Your " + command + " has been changed.")
    
def password_prompt():
    
    global player
    global items
    global rooms
    global GETs
    
    Finished = False
    
    while Finished != True:
        print("This computer is locked. Please enter a password: ")
        s = str(input())
    
        if s == items["computer"]["password"]:
            print("This Computer is unlocked..........")
            Finished = True
            rooms["Bathroom"]["items"].append(item_medication)
            items["computer"]["description"] = """The comptuer displays something...\nMedical records: \n Lives at home with their family of 4. 
Slight hint of psychosis when tested by therapist.
Given some medication for treatment, patient has stored it in the bathroom, dose of 1 pill per day."""
            typingprint.slow_print(items["computer"]["description"], True)
            typingprint.slow_print("""Just as you finish reading the information on the screen, you hear a quiet roaring noise which slowly builds in volume.
As the noise becomes deafening, the office fades from sight. 'I don't know where I am' you realise""", True)
            player["stage"] = 2
            GETs["computer used"] = True
        else:
            print("Incorrect Password")
            player["sanity"] -= 1
            break
    
    
def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    #Default response.
    printstr =  ""
    #If no command inputted.
    if 0 == len(command):
        return
    #Go command section
    if command[0] == "go":
        if len(command) > 1:
            printstr = execute_go(command[1])
        else:
            printstr =  ANSIstyles.RED + "Go where?" + ANSIstyles.END
    #Take command section
    elif command[0] == "take":
        if len(command) > 1:
            printstr = execute_take(command[1])
        else:
            printstr =  ANSIstyles.RED + "Take what?" + ANSIstyles.END
    #Drop command section
    elif command[0] == "drop":
        if len(command) > 1:
            printstr = execute_drop(command[1])
        else:
            printstr =  ANSIstyles.RED + "Drop what?" + ANSIstyles.END
    #Inspect command section
    elif command[0] == "inspect":
        if len(command) > 1:
            printstr = execute_inspect(command[1])
        else:
            printstr =  ANSIstyles.RED + "Inspect what?" + ANSIstyles.END
    #Use command section
    elif command[0] == "use":
        if len(command) > 1:
            printstr = execute_use(command[1])
        else:
            printstr =  ANSIstyles.RED + "Use what?" + ANSIstyles.END
    #If the command is meant to carry out a command outside the game, for example quiting the game.
    elif command[0] in ["quit","load","save"]:
        #Quit, load and save commands are handled in here.
        if command[0] == "quit":
            printstr = "quit"
        elif command[0] == "load":
            if len(save.list_saves()) > 0:
                load_game()
                printstr = "Loading"
            else:
                printstr = ANSIstyles.RED + "There are no saves to load!!" + ANSIstyles.END
        elif command[0] == "save":
            save.save(player, current_room, GETs, rooms)
            printstr = "Game saved!!!"
    else:
        #If the command is invalid, change the printstr to reflect so
        printstr = ANSIstyles.RED + "Invalid command!" + ANSIstyles.END
    #Return the created response to the users command
    return printstr

def return_exit(direction, leads_to):
    """This function returns a line to print_exits, these are then printed out in the standard menu format:"""
    return direction.upper() + " : " + leads_to + ".\n"

def print_exits(exits):
    printstr = ANSIstyles.RED + "There is nowhere you can go." + ANSIstyles.END + "\n"
    if len(exits) > 0:
        printstr = "You can " + ANSIstyles.YELLOW +  "GO:\n" + ANSIstyles.END
        for direction in exits:
            if is_valid_exit(exits,direction):
                printstr = printstr + return_exit(direction,exit_leads_to(exits, direction)["name"])
    if printstr == "You can " + ANSIstyles.YELLOW +  "GO:\n" + ANSIstyles.END:
        printstr = ANSIstyles.RED + "There is nowhere you can go." + ANSIstyles.END + "\n"
    typingprint.slow_print(printstr, type_print)

def print_take_item(items):
    """This function prints a menu of items which can be taken from the current room"""
    printstr = ""
    for item in items:
        if item["take"] == True:
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can " + ANSIstyles.YELLOW +  "TAKE:\n" + ANSIstyles.END + printstr[2::] + ".\n"
        typingprint.slow_print(printstr, type_print)

def print_drop_item(items):
    """This function prints a menu of items which can be dropped"""
    printstr = ""
    for item in items:
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can " + ANSIstyles.YELLOW +  "DROP:\n" + ANSIstyles.END + printstr[2::] + ".\n"
        typingprint.slow_print(printstr, type_print)

def print_use_item(items):
    """This function prints a list of items which can be used"""
    printstr = ""
    for item in items:
        if "use" in item and check_item_conditions(item):
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can " + ANSIstyles.YELLOW +  "USE:\n" + ANSIstyles.END + printstr[2::] + ".\n"
        typingprint.slow_print(printstr, type_print)

def print_inspect_item(items):
    """Prints list of items which can be inspected"""
    printstr = ""
    for item in items:
        if ("description" in item) or ("inspection" in item):
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can " + ANSIstyles.YELLOW +  "INSPECT:\n" + ANSIstyles.END + printstr[2::] + ".\n"
        typingprint.slow_print(printstr, type_print)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:"""
    try:
        return rooms[exits[direction]]
    except KeyError:
        return None

def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items:"""

    #Print exits
    print_exits(exits)
    #Print the items which you can take.
    print_take_item(room_items)
    #Print the items which you can drop.
    print_drop_item(inventory)
    #Print the items which you can use.
    print_use_item(inventory + room_items)
    #Print the items which you can inspect
    print_inspect_item(inventory + room_items)
    
    typingprint.slow_print("What do you want to do?", type_print)

def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:"""
    # Next room to go to=
    sound.play_exit_sound()
    return rooms[exits[direction]]

def reset_player():
    """This function resets the player dict to its default value"""
    #It is done like this instead of just assigning playerdefault to player as
    #Otherwise edits to player will be made to playerdefault
    #Preventing consequtive new games
    output = {}
    for item in playerdefault:
        output.update({item:playerdefault[item]})
    output["inventory"] = []
    return output

def reset_game():
    """This function resets all of the games variables to their default states"""
    global current_room
    global previous_room
    global player
    global inventory
    global rooms
    global GETs
    #Reset location
    current_room = rooms["Bedroom"]
    previous_room = ""
    #Reset player dictionary.
    player = reset_player()
    #Reassign inventory to the dict entry
    player["inventory"] = []
    inventory = player["inventory"]
    #Clear rooms of all items and add the default items for each room to that room.
    #This is done like this rather than assigning the default items value to items to prevent the editing of the default values.
    #This allows for the restarting of the game without restarting the whole program.
    for room in rooms:
        #Clear all items from each room.
        rooms[room]["items"] = []
        #Add each item to that room.
        for item in rooms[room]["items default"]:
            rooms[room]["items"].append(item)
    #Regenerate GETs with default values.
    GETs = generate_all_GETs()


def check_win_conditions():
    """This function checks whether win conditions have been met.
    If the win conditions are true then it will return true"""
    #Get the current stage from player dictionary
    stage = player["stage"]
    sanity_level = player["sanity"]
    Output = [False, False]
    #If the stage is greater than 5, the player wins
    if current_room == rooms["Outside"]:
        Output[0] = True
    #If sanity level is below -5, the player loses
    if sanity_level < -5:
        Output[1] = True
    return Output

def load_game():
    """Loads game from the selected option on the main menu"""
    global player
    global current_room
    global GETs
    global rooms
    option = mainmenu.menu(save.list_saves())
    everything = save.load(option)
    player = everything["player"]
    current_room = everything["room"]
    GETs = everything["GETs"]
    rooms = everything["rooms"]

# This is the entry point of our program
def main():
    #This loop allows the main menu to be reopened when we break out of the main game loop.
    while True:
        #These variables are edited during the loop, and so need the global keyword.
        global rooms
        global current_room
        global player
        global previous_room
        global type_print
        global GETs

        #If there are no saves, remove the load game option
        if len(save.list_saves()) > 0:
            option = mainmenu.menu(["New game ", "Load game", "Quit     "])
        else:
            option = mainmenu.menu(["New game ", "Quit     "])

        #Main menu logic
        if option.strip() == "Quit":
            quit()
        elif option.strip() == "Load game":
            load_game()
        elif option.strip() == "New game":
            reset_game()
        
        # Main game loop
        endstate = check_win_conditions()
        while endstate == [False, False]:
            #Clear screen at the begining of each loop
            if os.name == 'nt':
                os.system("cls")
            
            #Changes between each stage of the game are made here
            if player["stage"] >= 2 and player["stage"] < 7:
                current_room = rooms["Null"]
                previous_room = ""
                player["stage"] += 1
            if player["stage"] == 7:
                rooms["Bathroom"]["description"] = "You're back in the bathroom, you're not sure how you got here. You know you should take your meds, then get out of here."
                current_room = rooms["Bathroom"]
                player["stage"] += 1
            

            #Update type_print, this variable tells the program whether it should use the slow typing profile or not.
            type_print = not bool(previous_room == current_room)

            # Display game status (room description, inventory etc.)
            print_room(current_room)
            previous_room = current_room
            typingprint.slow_print(return_inventory_items(inventory),type_print)

            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["items"], inventory)

            if not os.name == 'nt':
                os.system('clear')
            
            # Execute the player's command
            command_return = execute_command(command)
            if command_return == "quit":
                break
            else:
                typingprint.slow_print(command_return, True)
            
            #If running on windows, pause (pause is not available on mac)
            if os.name == 'nt':
                os.system("pause")
                
            #Check win conditions
            endstate = check_win_conditions()

        #Display apppropriate end screen
        if endstate[0] == True:
            mainmenu.endscreen("win")
        elif endstate[1] == True:
            mainmenu.endscreen("lose")



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

