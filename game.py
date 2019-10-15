
from map import rooms
from player import *
from items import *
from gameparser import *
import os
os.system("mode con: cols=180 lines=50")


def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

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
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """
    items_in_room = list_of_items(room["items"])
    if not (items_in_room == ''):
        print("There is " + items_in_room + " here.")
        print("")

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """
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
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
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

