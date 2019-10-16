from items import *
from map import rooms
from gameparser import *

#Settings for max carry weight and starting inventory
max_carry_weight = 2
inventory = []

# Start game at the reception
current_room = rooms["Start"]

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
        print("Moving to " + current_room["name"])
    else:
        print("You cannot go there.")
    


def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """
    #Check if the player has enough space in their inventory to pick up the item.
    #If they dont print an error and return.
    inventory_mass = calc_inven_mass(inventory) + items[item_id]["weight"]
    if inventory_mass > max_carry_weight:
        print("You cannot carry any more.")
        return 0
    #Check if the item exists
    if item_id in items:
        item_id = items[item_id]
        if item_id in current_room["items"]:
            inventory.append(item_id)
            current_room["items"].remove(item_id)
            print("Picked up " + item_id["name"] + ".")
        else:
            print("You cannot take that.")
    else:
        print("That item does not exist.")
        
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """
    if item_id in items:
        item_id = items[item_id]
        if item_id in inventory:
            inventory.remove(item_id)
            current_room["items"].append(item_id)
            print("Dropped " + item_id["name"] + ".")
        else:
            print("You cannot drop that.")
    else:
        print("That item does not exist.")
    
def execute_inspect(item_id):
    """This function takes an item_id as an argument, then prints the description of that item.
    If the item does not exist then it prints "That item does not exist".
    """
    if item_id in items:
        item_id = items[item_id]
        if item_id in inventory:
            print(item_id["name"] + ":")
            print(item_id["description"])
        else:
            print("You cannot inspect that.")
    else:
        print("That item does not exist.")

def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")
    
    else:
        print("This makes no sense.")

def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:"""

    print("GO " + direction.upper() + " to " + leads_to + ".")

def print_take_item(item):
    """This function prints a line of a menu of items which can be taken"""
    print("TAKE " + item["id"].upper() + " to take " + item["name"] + ".")

def print_drop_item(item):
    """This function prints a line of a menu of items which can be dropped"""
    print("DROP " + item["id"].upper() + " to drop " + item["name"] + ".")



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

    print("You can:")
    # Iterate over available exits.
    for direction in exits:
        # Print the exit name and where it leads to.
        print_exit(direction, exit_leads_to(exits, direction))
    #Print the items which you can take.
    for item in current_room["items"]:
        print_take_item(item)
    #Print the items which you can drop
    for item in inventory:
        print_drop_item(item)
        
    
    print("What do you want to do?")

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

    # Next room to go to
    return rooms[exits[direction]]