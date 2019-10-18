
from map import rooms
from items import *
from gameparser import *
import os
import mainmenu
from player import *
import typingprint

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

def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:"""

    items_in_room = list_of_items(room["items"])
    if not (items_in_room == ''):
        print("There is " + items_in_room + " here.")
        print("")
    else:
        print("There are no items in this room.")
        print("")

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:"""

    items_in_inven = list_of_items(items)
    if not (items_in_inven == ''):
        print("You have " + items_in_inven + ".")
        print("")
    else:
        print("You don't have any items.")
        print("")


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:"""

    # Display room name
    print("\n" + room["name"].upper() + "\n\n" + room["description"] + "\n")
    print_room_items(room)


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
    #If item exists
    if item_id in items:
        item_id = items[item_id]
        #If item in inventory
        if item_id in inventory:
            #Remove the item from your inventory and then
            inventory.remove(item_id)
            current_room["items"].append(item_id)
            print("Dropped " + item_id["name"] + ".")
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
            print(item_id["name"] + ":")
            print(item_id["description"])
            #deep_inspect(item_id) Can be readded once items are fully finished
        else:
            #Return error message
            print("You cannot inspect that.")
    else:
        #Return error message
        print("You cannot inspect that.")

def execute_remember(remembering = ""):
    """Allows the player to recall things stored in their memory.
    Takes a string for input, will check if an entry with the same string exists in memory,
    if it does, then it will print what it stores.
    """
    #Check if remembering has a value.
    if remembering == "":
        #If remembering is empty, then print all items in memory.
        for memory in player["memory"]:
            print(memory + ": " + str(player["memory"][memory]))
    else:
        #If remembering does have a value, then
        try:
            #Print value of that memory
            print(remembering + ": " + player["memory"][remembering])
        #If the memory does not exist, print an error
        except KeyError:
            print("You don't seem to remember anything like that.")

def execute_use(item_id):
    """Allows player to use an item, takes item_id as an argument"""
    #Check if the item exists.
    if item_id in items:
        item_id = items[item_id]
        #Check if its in the players inventory
        if item_id in inventory:
            #Check if it's usable
            if "use" in item_id:
                pass 
                #Need code refering to effect of an item when used
                #Does using an item remove it from the inventory?
            else:
                #Tell the player they can't use it
                print("You cannot use that.")
        else:
            #Tell the player that it needs to be in their inventory
            print("Item must be in your inventory to use.")
    else:
        #Tell the player they can't use it
        print("You cannot use that.")

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

def check_win_conditions():
    """This function checks whether win conditions have been met.
    If the win conditions are true then it will return true"""
    
    #Need to add code to read definitions of win conditions
    Output = False
    return Output

# This is the entry point of our program
def main():
    # Main game loop
    win = False
    while win == False:
        os.system("cls")
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)

        #Check win conditions
        win = check_win_conditions()
        os.system("pause")
    os.system("cls")
    print("""
    ,,.*./././,***/,/,/,/,*,,*./././,*,,*,*.*./.*,*,.,.,./,(*//*/*(,(,/*/**/*(/#/#(#(###%#&#&#%##%#%(%(%/%(##(#(%#%(%#
    ,*,*./,(,(*//*(*(,(,/,**,,,*,/,/,/,**,/,/./.*,,,,*(#,/,/,/*,/*(*#*(*/*,,,*,/./,((###%#%#&#/.*,,*,/.#/%(####(%(%#&#
    **,/,##%%%%%%*(*#*#*(*/**/#%#%##((*//*/,/,#########%#%#%###//*(*#*#/(/**#%#%##,#####%(%#%#/,##%%##,#/%/#(#%(%#&#&#
    */*(,(,#%%%%%((,(*#*(**,###%##/(,(//(*/*######((/(/#/#/##%##%##,(*(/(/**#%#%##,####(%(%(%(/,###%##,#*#/#((#(%(&#&#
    */*(,(,#/#%%%##,(,(*(,((######,(*(////######(*///(*#*#*(/###%##/(.(*(/**#%#%##,((##(#/%/%//,###%##,(,(*(//(/%/%(%#
    **,/,(,(,#%#%##((./,/.(###(#,/./,/**/(#(#(/,*,/(/#/#*#*(*//(#(#((./,/*,,(###((,(((#/#/#*#*/,######./,(,/*//*#*%/%(
    ,*,*.(,(,/*(#(#(#(/.(((#(#(#.*./,*,,*(#(#(/./*//*(*(*(*(***(#(#(#(*.**,,(#(#(/,((((/#*(*(,*.(#(#((././,***/,(,#*#/
    ,,.*././,*.,*(#(((/ /#(#(#., *.*.,,/#(#(((* ****,*././,/,,,/#(#(((* *,..(#(#(/.///(*(*(,/,,.(#(#(/ *.*.*,,*,/,(,(*
    ..., *./.*,,,(#(((((((((.. , , ,.,./((((((* ,,,,., , *.*.,./#(((((, ,,..(#(#(*.*///*/,/./., (#(#(/ , *.,..,.*./.(*
    .. . * /.*,,,.,((((((((( . , , , ../((#(((, ,... . . , *.,.(((((((, **..(#(#(*.***/,/,/.*.. (#(#(* , , ,..,.,.*./,
    .. , * /.*,,,.*(#(((((. .,.* * , ,./((#(((* ,... . . , ,.,.(#(#(((, */..(#(#(* ***/,/,/.*.. (#(#(/ , , ,..,.*.*./.
    ,,.,.*./.*,**,*./(#(#(,.,*.*.* *.,..,(#(#(* ,.,,., , , ,.,,(#(#(#(* //..(#(#(/./***,/,/.*.,.(#(#(/ *.*.*,,*,*././,
    **,/.(,(,/*//*/./#####,.*/,/,/./.*,,*####(#(*.,,.*.*.*.*.**(###(/.*.(/,,(####/./*//**,/.*.*.#####(././,/**/*(,(,(,
    //*(,(,#*(*////,(#####*,/(*(,(,/,/***(######/,,,,*.*././*######(/.((#(,,(###((#/*/*,/,/,/,######((./,(*(//(/#*#*#*
    //*(*#*#/#/((/(,(#%###*,/(/#*#*(*/**/,((######/**/*(*(*######((./,#(#(**,/#%#(##(////*(*########,/,#*#/#(##(%/%*#/
    /(*(*#*(/#/((/(,##%###*,/(/#*#*#*(///*/,(/(/#########%#%###((,(*#/#(#((#*(/(/#((((((########(//(*#/%/%(%##%(%/%/%/
    //*(*#*(/#/(//(,(*(*/***/(*(*#*(*(///*/,/././*//*/*(*(*(////(*#/%/#/#/*(*(,/,(*(////(*(*(*/***/(/#/%/%(###%(%/%/%(
    **,*,#,/*(*//**,/,/,*.,,,**(,(*(,****,/,/./,*.,,,*.*.*,(*///(/(*/,/*(***,*.*./,/,,*,*,/.*.*,*,*/*#/#/#((//(*(/#/#/
    .,,*./.*,/*/*,/,/./.,.,,.,.*./,*,/***.,.*.*.,,,,.,.*.*.,,*,,*,,./.*.*,.,.*.*.*.*.,*,*,,.*.*..,,*.,,/,(*//**,*././.
    .,(#(#(*.*,,,,*.*.* /#///#(( *.*,*,,*.,/(((//(....(#(#//#(#(#(//((, ,..,(((((#((/.,.,..., , .,(#/((/./,**,*/#(#(* 
     .(###/(#*.,,.*.* * *((#(#(( *.*.*,,,.,/(((/,... .(((#//#(#(#///((, .. .(#(//#((/.,.,.. . ,  .(#//(/ /,*,,/(#(#(, 
    .. ./((##*.,..*., /(////////.,.*.,..*.,/(((/. .. . , *./#((// , , . ....///(##((///.,.. . ,  .(#(((/ *,*..,/(##(, 
    ...,#####*.,,.,., /((((#(#(#(/ *,*,,,(#(#(((, ..., , *,##(#((., , , . ..(#(#(#((#(((* , , . ..(#(#(/ *,*,,/####(* 
    .,.,#%#%#/,,,,*.* ((##((##(#((.*,**,*(#(#(* ,...., , /,#####(.,., ,.,...(#(#(#(####(/., , , ..####(/./,/,,/###%#*.
    ,,.*#%#%#%#**,*./.(##(,.(####(./*/***####(/.*.,,.,.*./*#####(.*.*./.*,,,(###((.*,####(/.*.,.,,#####(./*(**/#%#%#/.
    **,/,(#%#%#/**/,(#%###*,,*####,(*(/*/#%#%#/.*.,,,*./.(/######,/./,/,*,,*#####(,/,(#####(/.*.*,###%##,(/#//(%%%%#(,
    **,/,##%%%#//*(,##%##/*,,*#%#%#(,/*/(#%##//./,*,,*,/.(/%#%###,/,(,/,/,,*###%#(,/*//###%#(*/,*,#%#%##,#/#(/(%%%%#(,
    //*(,##%%%%((*(,(#%#/,//,*#%#%#(,/*###%#(,/.*,**,*,/,(/######,/,(,/,*,,*###%#(,/*///######/,((#%#%##,#(#(/(#%#%#(,
    //*(,(*###%##*((####/,//*/*(###(,/*(###((./.*,*,,*./.(/######,/,/./,*,,*(####(,/****/*(###((###%#%##,#(#(/(#%#%#(,
    */,(,(.(##%#%(######*.//*/.*(###((#(#(#((.*.*.,,.,.*./*##(#((,*.*.*.,.,,(#(#((.*,**,*.((####(####%((,(/(/*/*/,/,/.
    **,/,/.(###(#(#(#(/.*,***/.*(##(#(#(#((.*.* ,...., ,./,(#(#((.*.* ,.,..,(#(#(/.*,,,,*.*.(((#(#(#(#((./*/**/,/,/./.
    **,/,/ *./#(#(#(#(/ *****/ ,.(((#(#(#(( , , . .. . , *.(#(#((., , , ....(#(#(*.,,,,.*., /((#(#(#(#(/.*,*,,,.*.* * 
    ,*,/,(,* /#(#(#(#(* **//*/,/ *((#(#(#(/ , , . .  .(#(#((#(#(#(((((, ....(#(#(* ,,,,.*.* , (((#(#(#(/ *.*../(###(, 
    */*(*(*/ (#####(( * /////(*/ *(##(#(#*/ , * , .. .(#(#((#(#(#(#(((, ....(#(#(* *,,*,*.*., . (#####(/ *.,../####(* 
    /(/(/#/(.*.,,.*.*.//((///(/( *.*.,..,.*,/./.*.,... , , ,.,..,., , , ,...., , *.*,*/*(*(*(,, .... , *.*.*,,,.*.* * 
    (((#(%(%(%#####(#(#(#(#((#(#/#/#/((((/(*(*(,/***,*././,/,/**/*(,(,/,*,**,/,/,(,///(/#/#/#/(*/***,/.(./,*,**,*././.
    """)
    os.system("pause")



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

