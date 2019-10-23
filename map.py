from items import *

room_bedroom = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Bedroom",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """In a large cozy room with not too many items you
    only find a bed, a nightstand and a wardrobe. There is
    a big window near your bed. A dim light comes from
    outside but soon it disappears.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"north": "Bathroom", "west": "Hallway"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_window, item_wardrobe, item_matches, item_candle, item_clock]
}

room_bathroom = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Bathroom",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """As you open the door you see a dim light. It's just
    a reflection. You can only approach the mirror as you
    cannot see anything else... .The mirror is placed on
    a drawer that you cannot open. There is a black window
    near the sink.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Bedroom"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_mirror, item_writing_on_wall, item_medication]
}

room_hallway = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Hallway",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """Long and empty with an old wood floor, the hallway leads you to other two
    rooms: the kitchen and the living room. Hopefully the exit is near.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"east": "Bedroom", "west": "Lounge", "north": "Kitchen", "south": "Outside"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_coat, item_fusebox, item_vase, item_door]
}

room_living_room = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Lounge",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """It looks like nothing you saw untill now. You can see your reflection in
    the marble floor. Near an armchair there is a table with a fruit bowl on it.
    The fruits are fresh but the air has a rotten smell.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"east": "Hallway", "north": "Office"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_picture, item_fuse, item_wall_markings, item_magnifying_glass]
}

room_office = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Office",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """A short, cold breeze washes the rotten smell away. You can see a blue light
    on a computer screen. The window is oppened but you see nothing but a sea shore filled with weird objects.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Lounge"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_book, item_computer, item_paper]
}

room_kitchen = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Kitchen",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """Is this childhood? Old products on the shelf, same cutlery from 30 years ago.
    Is this a dream or a nightmare? Nothing makes sense.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Hallway"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_knife, item_bowl, item_painting]
}

room_outside = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Outside",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """You are out on a field. The house has disappeared.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"north": "Hallway"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": []
}

room_null = {
    "name": "Null",

    "name": "????",

    "description": """You don't recognise this place, you decide to continue looking for the bathroom...
Although you have no idea where to start...""",

    "exits": {"north": "Null", "south": "Null", "west": "Null", "east": "Null"},
    
    "items": [],
    "items default": []
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
    "Outside": room_outside,
    "Null": room_null
}