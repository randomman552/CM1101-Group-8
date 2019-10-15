from items import *

room_example = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Example",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is an example room.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {},
    #Items contains a list of the items available in the room on game start.
    "items": [item_example],
    #Win conditions is used to contain a list of win conditions associated with the room (work in progress).
    "win conditions": {
        "items": []
    }
}

#Contains all of the rooms in the game with an identifier.
#For example, "Start": room_example.
rooms = {
    "Start": room_example
}