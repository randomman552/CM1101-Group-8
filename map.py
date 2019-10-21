from items import *

room_bedroom = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Bedroom",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is your bedroom""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"north": "Bathroom", "west": "Hallway"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_mirror,item_window]
}

room_bathroom = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Bathroom",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is your bathroom""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Bedroom"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_medication,item_window]
}

room_hallway = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Hallway",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is the hallway""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"east": "Bedroom", "west": "Lounge", "north": "Kitchen", "south": "Outside"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_coat]
}

room_living_room = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Lounge",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is the living room""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"east": "Hallway", "north": "Office"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_family_picture,item_window]
}

room_office = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Office",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is your office""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Lounge"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_book,item_window]
}

room_kitchen = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Kitchen",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is the kitchen""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Hallway"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_knife,item_window]
}

room_outside = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Outside",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """This is outside?""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"north": "Hallway"},
    #Items contains a list of the items available in the room on game start.
    "items": []
}

#Contains all of the rooms in the game with an identifier.
#For example, "Start": room_example.
rooms = {
    "Bathroom": room_bathroom,
    "Bedroom": room_bedroom,
    "Hallway": room_hallway,
    "Lounge": room_living_room,
    "Office": room_office,
    "Kitchen": room_kitchen,
    "Outside": room_outside
}