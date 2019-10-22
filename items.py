item_medication = {
    #id of the room, is used as its name
    "id": "medication",
    #Name is shown when listing items from inventory
    "name":
    "your medication",
    #Take states if an item can bee stored in the inventory or not
    "take": True,
    #Description can be read with inspect command
    "description":
    """A small, white jar with your name on it. There
are pills inside. They look like Skittles""",
    #Inspection can be made with other items
    "inspection":
    "Nothing weird about them",
    #'use' atribute tells the player if he/she can use
    #the item and what happens after
    "use": {
        #Conditions sets what conditions must be true in order for the item to be usable. 
        #These conditions are added automatically to the GETs system.
        "conditions": { 
            "fuse box": True
        },
        #Text is printed when the item is used
        "text": """You shake the bottle and the last two pills fall out.
You swallow the pills quickly, and get ready to move on.""",
        #This dictates how the usage of an item will affect the GETs system.
        "GETs effect":{
            "power": False
        },
        "stage effect": 0,
        "psychosis effect": 0,
        "remove after use": True,
        "items": []
    }
    }

item_book = {
    "id": "book",
    
    "name": "an old book",
    
    "take": True,
    
    "description":
    """An old book, covered in dust. Laying on the floor.""",
    
    
    "inspection":
    """ A page is missing. You notice that on page 14 your name is written in bold on the end.""",
    }

item_family_picture = {
    "id": "picture",

    "name": "a family picture",

    "take": False,

    "description":
    "A family picture from your last birthday",

    "inspection":
    """There is a number on the back of the frame. You can
recognize everybody, but you can't remember their names."""
    }

item_knife = {
    "id": "knife",

    "name": "a simple kitchen knife",

    "take": True,

    "description":
    """An old knife. It's obviously been here for a while, but you've not used it yet. 
You can't remember why.""",

    "use": {
        "conditions": {},
        "text": "You don't want to do that.",
        "stage effect": 0,
        "psychosis effect": 0,
        "remove after use": False,
        "items": []
    }
    }

item_mirror = {
    
    "id": "mirror",

    "name": "a mirror",

    "take": False,

    "description": "A shiny mirror",

    "inspection": 
    """All you can see is your purpose, a question: 
'Who are you?' """,

    "use": {
        "conditions": {},
        "text": "You see yourself reflected in the mirror.",
        "stage effect": 0,
        "psychosis effect": 0,
        "remove after use": False,
        "items": [item_knife]
    }
    }
    
item_window = {
    "id": "window",
    
    "name": "a window",
    
    "take": False,
    
    "description":
    """A slightly open window. You can hear the wind whistle past,
but you don't see anything of particular interest."""
}

item_coat = {
    
    "id": "coat",

    "name": "your coat",

    "take": True,

    "description": """Your coat, you remember wearing this on countless rainy days.
You do live in wales after all.""",

    "use": {
        "conditions": {},
        "text": "You put the coat on, you find its warmth comforting.",
        "stage effect": 0,
        "psychosis effect": -1,
        "remove after use": True,
        "items": []
    }
    }

#Contains a list of all items in the game, with an identifier.
#Items must be put in this list to be usable.
#Item should be put in like this: "example": item_example
items = {
    "medication": item_medication,
    "mirror": item_mirror,
    "picture": item_family_picture,
    "knife": item_knife,
    "book": item_book,
    "family picture": item_family_picture,
    "window": item_window,
    "coat": item_coat
    }