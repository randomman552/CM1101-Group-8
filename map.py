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
    "items default": [item_window, item_wardrobe, item_candle, item_clock],
    "conditions":{

    }
}

room_bathroom = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Bathroom",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """As you open the door you see a dim light. It's just
a reflection on the mirror. You can only approach the mirror as you
cannot see anything else... .The mirror is placed on
a drawer that you cannot open.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Bedroom"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_mirror, item_writing_on_wall],
    "conditions":{
        "candle": True
    }
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
    "items default": [item_coat, item_fusebox, item_vase, item_door],
    "conditions":{
        "candle": True
    }
}

room_living_room = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Lounge",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """It looks like nothing you saw untill now. You can see your reflection in
the marble floor. Near an armchair there is a table with a fruit bowl on it.
The fruits are fresh but the air has a rotten smell.
You can see the office door, but it's locked.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"east": "Hallway", "north": "Office"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_picture, item_fuse, item_wall_markings, item_magnifying_glass],
    "conditions":{
        
    }
}

room_office = {
    #The name of the room, this is shown on screen when the player is in the room.
    "name": "Office",
    #Description of the room, this is shown on screen when the player is in the room.   
    "description":
    """Using the key you enter the office, on the desk at the far end you see a computer.
You will need to get the power back on before using it.""",
    #Exits contains the available exits from the room, this must be set in order for the player to leave the room.
    "exits": {"south": "Lounge"},
    #Items contains a list of the items available in the room on game start.
    "items": [],
    "items default": [item_book, item_computer, item_paper],
    "conditions":{
        "items": [item_key]
    }
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
    "items default": [item_knife, item_bowl, item_painting],
    "conditions":{
        
    }
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
    "items default": [],
    "conditions":{
        "outside open": True,
        "coat on": True
    }
}

room_null = {
    "name": "Null",

    "name": "????",

    "description": """You don't recognise this place, you decide to continue looking for the bathroom...
Although you have no idea where to start...
Dark shapes shift at the edges of your vision, you are afraid.""",

    "exits": {"north": "Null", "south": "Null", "west": "Null", "east": "Null"},
    
    "items": [],
    "items default": [],
    "conditions":{
        "outside open": True
    }
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