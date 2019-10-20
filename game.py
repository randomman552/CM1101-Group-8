from map import rooms
from items import items
from gameparser import *
import os
import mainmenu
import sound
os.system("mode con: cols="+ str(mainmenu.maxwidth) + " lines="+ str(mainmenu.maxheight))
from player import *
import typingprint
import pygame

#Initialise pygame and and its mixer in the main thread.
pygame.init()
pygame.mixer.init()
#Start background music, can be stopped at any point by calling BG_Music(False)
sound.BG_Music()

#type_print is a global variable that is used to define whether printing is instant or not.
#for example, typingprint.slow_type("Hello", type_print) would print instantly if print_type was true, and type it if false.
#this is used so that if the user has not changed room, the text is not typed out again.
type_print = True

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
        return "There is " + items_in_room + " here."
    else:
        return ""

def return_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely in a string.
    It then returns this string to be used elsewhere.
    """

    items_in_inven = list_of_items(items)
    if not (items_in_inven == ''):
        printstr = "You have " + items_in_inven + "."
    else:
        printstr = "You don't have any items."
    return printstr


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this)."""

    # Display room name
    printstr = "\n" + room["name"].upper() + "\n" + room["description"]
    typingprint.slow_print(printstr,type_print)
    typingprint.slow_print(return_room_items(room),type_print)


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:"""

    return chosen_exit in exits

def calc_inven_mass(inventory):
    """Calculates the mass of all items in the players inventory"""
    Output = 0
    for item in inventory:
        Output += item["weight"]
    return Output

def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    if is_valid_exit(current_room["exits"],direction):
        current_room = move(current_room["exits"],direction)
        typingprint.slow_print("Moving to " + current_room["name"])
    else:
        typingprint.slow_print("You cannot go there.")

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    #Check if the item exists
    if item_id in items:
        item_id = items[item_id]
        if item_id["take"] == True:
            if item_id in current_room["items"]:
                inventory.append(item_id)
                current_room["items"].remove(item_id)
                typingprint.slow_print("Picked up " + item_id["name"] + ".")
            else:
                print("You cannot take that.")
        else:
            print("You cannot take that.")
    else:
        print("You cannot take that.")

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    #If item exists
    if item_id in items:
        item_id = items[item_id]
        #If item in inventory
        if item_id in inventory:
            #Remove the item from your inventory and then
            inventory.remove(item_id)
            current_room["items"].append(item_id)
            typingprint.slow_print("Dropped " + item_id["name"] + ".")
        else:
            print("You cannot drop that.")
    else:
        print("That item does not exist.")

def deep_inspect(item_id):
    """This function provides further information about an item if certain items are present in the players inventory"""
    #if item_magnifying_glass in inventory:
        #print(item_id["inspection"])

def execute_inspect(item_id):
    """This function takes an item_id as an argument, then prints the description of that item.
    If the item does not exist then it prints "That item does not exist".
    """
    #If the item exists
    if item_id in items:
        #Retrieve actual itme id from items list
        item_id = items[item_id]
        #If item is in inventory or in the current room
        if item_id in inventory or item_id in current_room["items"]:
            #Print item description
            printstr = item_id["id"] + ":\n" + item_id["description"]
            #deep_inspect(item_id) Can be readded once items are fully finished
        else:
            #Return error message
            printstr = "You cannot inspect that."
    else:
        #Return error message
        printstr = "You cannot inspect that."
    typingprint.slow_print(printstr, True)

def execute_remember(remembering = ""):
    """Allows the player to recall things stored in their memory.
    Takes a string for input, will check if an entry with the same string exists in memory,
    if it does, then it will print what it stores.
    """
    #Check if remembering has a value.
    if remembering == "":
        #If remembering is empty, then print all items in memory.
        for memory in player["memory"]:
            typingprint.slow_print(memory + ": " + str(player["memory"][memory]), True)
    else:
        #If remembering does have a value, then
        try:
            #Print value of that memory
            typingprint.slow_print(remembering + ": " + player["memory"][remembering], True)
        #If the memory does not exist, print an error
        except KeyError:
            typingprint.slow_print("You don't seem to remember anything like that.", True)

def execute_use(item_id):
    """Allows player to use an item, takes item_id as an argument"""
    #Check if the item exists.
    if item_id in items:
        item_id = items[item_id]
        #Check if its in the players inventory
        if (item_id in inventory) or (item_id in current_room["items"]):
            #Check if it's usable
            if "use" in item_id:
                printstr = item_id["id"] + ":\n" + item_id["use"]["text"]
                if item_id["use"]["remove after use"]:
                    if item_id in inventory:
                        inventory.remove(item_id)
                    elif item_id in current_room["items"]:
                        current_room["items"].remove(item_id)
            else:
                #Tell the player they can't use it
                printstr = "You cannot use that."
        else:
            #Tell the player they can't use it
            printstr = "You cannot use that."
    else:
        #Tell the player they can't use it
        printstr = "You cannot use that."
    typingprint.slow_print(printstr, True)

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return
    #Go command section
    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
    #Take command section
    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
    #Drop command section
    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
    #Inspect command section
    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")
    #Remember command section
    elif command[0] == "remember":
        if len(command) > 1:
            execute_remember(command[1])
        else:
            execute_remember()
    #Use command section
    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")
    #If none of the above commands are entered, print an error.
    else:
        print("This makes no sense.")

def print_item_unified():
    pass

def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:"""
    typingprint.slow_print("GO " + direction.upper() + " to " + leads_to + ".", type_print)

def print_take_item(items):
    """This function prints a menu of items which can be taken from the current room"""
    printstr = ""
    for item in items:
        if item["take"] == True:
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can TAKE:\n" + printstr[2::]
        typingprint.slow_print(printstr, type_print)

def print_drop_item(items):
    """This function prints a menu of items which can be dropped"""
    printstr = ""
    for item in items:
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can DROP:\n" + printstr[2::]
        typingprint.slow_print(printstr, type_print)

def print_use_item(items):
    """This function prints a list of items which can be used"""
    printstr = ""
    for item in items:
        if "use" in item:
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can USE:\n" + printstr[2::]
        typingprint.slow_print(printstr, type_print)

def print_inspect_item(items):
    """Prints list of items which can be inspected"""
    printstr = ""
    for item in items:
        if ("description" in item) or ("inspection" in item):
            printstr += ", " + item["id"]
    if not(printstr == ""):
        printstr = "You can INSPECT:\n" + printstr[2::]
        typingprint.slow_print(printstr, type_print)

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:"""

    return rooms[exits[direction]]["name"]

def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items:"""

    typingprint.slow_print("You can:", type_print)
    # Iterate over available exits.
    for direction in exits:
        # Print the exit name and where it leads to.
        print_exit(direction, exit_leads_to(exits, direction))
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

def check_win_conditions():
    """This function checks whether win conditions have been met.
    If the win conditions are true then it will return true"""
    
    #Need to add code to read definitions of win conditions
    Output = False
    return Output
def reset_game():
    global current_room
    global previous_room
    global player
    global inventory
    current_room = rooms["Bedroom"]
    previous_room = ""
    player = playerdefault
    inventory = []

# This is the entry point of our program
def main():
    #This loop allows the main menu to be reopened when we break out of the main game loop.
    while True:
        option = mainmenu.menu(["New game ", "Load game", "Quit     "])
        if option.strip() == "Quit":
            quit()
        elif option.strip() == "Load game":
            mainmenu.menu(["SAVES LIST HERE"])
            #Need loading code before implementation.
        elif option.strip() == "New game":
            reset_game()
        # Main game loop
        win = False
        while win == False:
            global previous_room
            global type_print
            os.system("cls")

            #Update type_print
            type_print = not bool(previous_room == current_room)

            # Display game status (room description, inventory etc.)
            print_room(current_room)
            previous_room = current_room
            typingprint.slow_print(return_inventory_items(inventory),type_print)

            # Show the menu with possible actions and ask the player
            command = menu(current_room["exits"], current_room["items"], inventory)

            
            # Execute the player's command
            if command[0] in ["quit","load","save"]:
                #If the command is meant to carry out a command outside the game, for example quiting the game.
                if command[0] == "quit":
                    break #Breaks out of the loop, and starts the main menu again
                elif command[0] == "load":
                    pass #Call load function
                elif command[0] == "save":
                    pass #Call save function
            else:
                #If the command is meant to be carried out within the game.
                execute_command(command)
            
            #Check win conditions
            win = check_win_conditions()

            os.system("pause")



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

