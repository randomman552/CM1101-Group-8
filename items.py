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
    "use":
    "You took two pils. Do you think it's enough?",
    }

item_book = {
    "id": "book",
    
    "name": "an old book",
    
    "take": True,
    
    "description":
    """An old book, covered in dust. Laying on the floor.""",
    
    
    "inspection":
    """ A page is missing. You notice that on page 14 your
name is written in bold on the end.""",
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

    "take": False,

    "description":
    """An old knife. It's there since ever, but you never
use it, did you?""",
    }

item_mirror = {
    
    "id": "mirror",

    "name": "a mirror",

    "take": False,

    "description": "A shiny mirror",

    "inspection": 
    """All you can see is your purpose, a question: 
        'Who are you?' """,

    "use": "You break through a reality that's no longer here.",
    }
    
item_window = {
    "id": "window",
    
    "name": "a window",
    
    "take": False,
    
    "description":
    """A slightly open window. You can hear the wind
but you won't see anything"""
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
    "family picture": item_family_picture
    }