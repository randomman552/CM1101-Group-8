
from map import rooms
from player import *
from items import *
from gameparser import *
import os
os.system("mode con: cols=180 lines=50")


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

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:"""

    items_in_inven = list_of_items(items)
    if not (items_in_inven == ''):
        print("You have " + items_in_inven + ".")
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

