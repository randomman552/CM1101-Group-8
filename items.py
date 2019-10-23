
def caesar_cipher(text, shift):
  characters = [char for char in text]
  return ''.join(list(map(lambda character: 
    ' ' if ord(character) == 32 else chr((ord(character) + shift - 97) % 26 + 97),
    characters)))


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
    """A small, white jar with my name on it. There
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
            "computer used": True
        },
        #Text is printed when the item is used
        "text":
        """You shake the bottle and the last two pills fall out.
        You swallow the pills quickly, and get ready to move on.""",
        #This dictates how the usage of an item will affect the GETs system.
        "GETs effect":{
            "door unlocked": True
        },
        
        "stage effect": 0,
        
        "psychosis effect": 0,
        
        "remove after use": True,
        
        "items": []
    }
    }

item_mirror = {
    "id": "mirror",

    "name": "a mirror",

    "take": False,

    "use": {
        "conditions": { 

        },
        "text": """""",
        
        "GETs effect":{
            
        },
        
        "stage effect": 1,
        
        "psychosis effect": 0,
        
        "remove after use": False,
        
        #Item given elsewhere in the main code
        #"items": [item_key]
        }
    }

item_writing_on_wall = {
    "id": "writing",

    "name": "a word on the wall",

    "take": False,

    "description":
    """A jumbled mess of letters. I'm not sure what
    it's supposed to mean.""",

    "inspection":
    """Nothing more than letters. I have to
    figure this out, might be a name...""",

    "use": {
        "conditions": { 
            "magnifier": True
        },
        "text":
        """Those letters are jumbled. Can't be too hard... """ + caesar_cipher("Sam", 1) ,

        "GETs effect": {

            },
        
        "stage effect": 1,
        
        "psychosis effect": 0,
        
        "remove after use": False,
        
        "items":[]
        }
    }

item_candle = {
    "id": "candle",

    "name": "a candle",

    "take": True,

    "description":
    """A wax candle. Could be a light source.
There are some matches next to it.""",

    "inspection":
    """Just a normal wax candle""",

    "use": {
        "conditions": { 

        },

        "text":
        """You have a light source now. You can see two
doors. One leads to a bathroom for sure. 
You take the candle and get ready to move on.""",

        "GETs effect": { 
            "candle": True
        },
        
        "stage effect": 1,
        
        "psychosis effect": 0,
        
        "remove after use": True,
        
        "items":[]
        }
    }

item_clock = {
    "id": "clock",
    
    "name": "an alarm",
    
    "take": False,
    
    "description":
    """A simple alarm clock on your nightstand. I wonder when
    is it going to ring?""",

    "inspection":
    """I hope it rings and the nightmare will be gone.""",
    
    "use": {
         
        
        "text":
        """You push the buttons but nothing happens.

        
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |     __       | || |    _____     | || |              | || |   _    _     | || |     ____     | |
| |    /  |      | || |   / ___ `.   | || |      _       | || |  | |  | |    | || |   .'    '.   | |
| |    `| |      | || |  |_/___) |   | || |     (_)      | || |  | |__| |_   | || |  |  .--.  |  | |
| |     | |      | || |   .'____.'   | || |      _       | || |  |____   _|  | || |  | |    | |  | |
| |    _| |_     | || |  / /____     | || |     (_)      | || |      _| |_   | || |  |  `--'  |  | |
| |   |_____|    | || |  |_______|   | || |              | || |     |_____|  | || |   '.____.'   | |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' """,
        "GETs effect": {

        },
        
        "stage effect": 1,
        
        "psychosis effect": 0,
        
        "remove after use": False,
        
        "items":[]
    }
}

item_window = {
    "id": "window",
    
    "name": "a window",
    
    "take": False,
    
    "description":
    """A slightly open window... I hear the wind whistle past,
    but I don't see anything of particular interest.""",

    "inspection":
    """There are 0s and 1s on the window frame."""
    }

item_red_scarf = {
    "id": "scarf",

    "name": "a red scarf",

    "take": True,

    "weight": 0,

    "description":
    """This is my red scarf.""",

    "inspection":
    """Oh it has some 0s and 1s on it."""
    }
    
item_wardrobe = {
    "id": "wardrobe",
    
    "name": "a wardrobe",
    
    "take": False,
    
    "description":
    """A wardrobe... Are those my clothes? Maybe I can find something.""",

    "inspection":
    """We have to open it to see more.""",

    "use": {
        "conditions":{
            "candle": True
        },

        "text":
        """Opening the wardrobe i see a red scarf, looks like it's straight out of Hogwarts. 
It's more familiar than I care to admit, Perhaps it's a clue?""",

        "GETs effect": {
            "scarf found": True
        },

        "stage effect": 0,

        "psychosis effect": 0,

        "remove after use": True,

        "items": [item_red_scarf]
        }
    }

item_coat = {
    "id": "coat",

    "name": "your coat",

    "weight": 1,

    "take": True,

    "description": 
    """It's this my coat? I remember wearing this on all those rainy days...
    I live in Wales after all.""",

    "inspections":
    """Nothing in the pokets, I feel like something is missing.""",

    "use": {
         
        
        "text": "You put the coat on, you find its warmth comforting.",
        
        "GETs effect": {"power": False},
        
        "stage effect": 1,
        
        "psychosis effect": -1,
        
        "remove after use": True,

        "items":[]
        }
    }

item_fuse = {
    "id": "fuse",

    "name": "a fuse",

    "take": True,

    "weight": 0,

    "description":
    """A fuse… Who removed it?""",

    "inspection":
    """I need to put it back."""
    }

item_fusebox = {
    "id": "fusebox",
    
    "name": "a fusebox",
    
    "take": False,
    
    "description":
    """A red fusebox on the wall...""",
        
    "inspection":
    """I need a fuse to power up the house""",
    
    "use": {
        "conditions": {
            "items":[item_fuse]
        },
        
        "text":
            """You open it and push back in its place.
        The lights are now on. You can get rid of that candle.
        Everything is more clear now, but... you cannot see
        anything that might help you.""",

        "GETs effect": {"computer on": True},
        
        "stage effect": 0,
        
        "psychosis effect": 0,
        
        "remove after use": False,

        "items":[]
        }
    }

item_vase = {
    "id": "vase",

    "name": "a red vase",

    "take": False,

    "description":
    """A vase filled with dead flowers. How long have
    these been here?I never was good at looking
    after things.""",

    "inspection":
    """I should throw those flowers away after
    I figure out what is going on."""
    }

item_picture = {
    "id": "picture",

    "name": "a family picture",

    "take": False,

    "weight": 1,

    "description":
    """I remember every face but this one... I can't recall any name though.""",

    "inspection":
    """This one is very familiar. I feel like I am somehow related to him.""",

    "use": {
        "conditions":{
            "scarf found": True
        },

        "text":
        "",

        "GETs effect": {"power": False},

        "stage effect": 0,
        
        "psychosis effect": 0,

        "remove after use": False,

        "items":[]
        }
    }

item_key = {
    "id": "key",
    
    "name": "a key",
    
    "take": True,

    "weight": 0,
    
    "description":
        "A small key. I wonder what it opens...",
        
    "inspection":
        "It's just a small key",
    
    "use": {
        "conditions": { 
            "items": [item_picture],
            "comptuer on": True
        },

        "text":
        """You open the office door, expecting
        for answers but you can only see a blue light
        on an old desk.""",
        
        "GETs effect":{
            "office open": True
        },
        "psychosis effect": -1,
        
        "remove after use": True,
        
        "items": [item_medication]
        }
    }

item_wall_markings = {
    "id": "markings",

    "name": "some lines on the wall",

    "take": False,

    "description":
    """Those have to be related with height. I wonder which one fits me.""",

    "inspection":
    """Let's see...


                       _     _____   ___  
                      / |   |___  | / _ \ 
 _____  _____  _____  | |      / / | | | |
|_____||_____||_____| | | _   / /  | |_| |
                      |_|(_) /_/    \___/ 
                                          """,
    }

item_magnifying_glass = {
    "id": "magnifier",

    "name": "a magnifier",
    "take": True,

    "weight": 0,

    "description":
    """I might be able to use this help with inspecting things...""",

    "use": {
        "text":
        "Now I should be able to inspect things better...",

        "GETs effect": {
            "magnifier": True
        },

        "stage effect": 0,
        
        "psychosis effect": 0,

        "remove after use": True,

        "items":[]
        }
    }

item_book = {
    "id": "book",
    
    "name": "a book",
    
    "take": True,

    "weight": 1,
    
    "description":
    """An old burned book. Just a few pages left.""",
    
    "inspection":
    """An unfortunate looking book. Only the pages 1, 2, 6, 21, 88 are left.
    There's one more page, much further in the book, but the number's
    been burnt off. Huh."""
    }

item_paper = {
    "id": "paper",

    "name": "a scrap of paper",

    "take": True,

    "weight": 0,

    "description":
    """A scrap of paper...why does it also looks old?
    Everything seems to be a memmory.""",

    "inspections":
    """On the scrap is written "Often will I spin a tale,
    never will I charge a fee. I'll amuse you an entire
    eve, but, alas you wont remember me. What am I?"
    Who writes this stuff?"""
    }

item_computer = {
    "id": "computer",

    "name": "a computer",

    "take": False,

    "description":
    """An old computer, the light is so intense. How did it end up here?""",

    "inspection":
    """It looks like my first computer.""",

    "use": {                
        "conditions": {
            "computer on": True
        },

        "text": """ """,

        "GETs effect": {
            
        },

        "stage effect": 2,

        "psychosis effect": 1,

        "items":[]
        },
    "password" : "dream445",
    }

item_knife = {
    "id": "knife",

    "name": "a simple kitchen knife",

    "take": True,

    "weight": 1,

    "description":
    """A kitchen knife. It's very, very sharp.""",
    

    "use": {
         
        
        "text": "Really? You hate the game THAT much?",

        "GETs effect": {},
        
        "psychosis effect": -6,
        
        "remove after use": False,
        }
    }

item_bowl = {
    "id": "bowl",

    "name": "a bowl of noodles",

    "take": True,

    "description":
    """Just like mom used to make: quick, tasty and… Freshly-made.
    Where did these come from?""",

    "inspection":
    """It feels like a memmory.""",

    "use": {
         

        "text":
        """It also tastes like my moms. Weird.""",

        "GETs effect": {},
        
        "psychosis effect": 1,
        
        "remove after use": True,

        "items":[]
        }
    }

item_painting = {
    "id": "painting",

    "name": "a painting",

    "take": False,

    "description":
    """The painting reads "Retro Bazinger!".
    It looks like someone was a fan of computer games.""",

    "inspection":
    """Nothing more than a comic page in a frame."""
    }
  
item_door = {
    "id": "door",
    
    "name": "exit door",
    
    "take": False,
    
    "description": 
        """This door seems to be the answer to everything.
        We have to figure this out.""",
        
    "use": {
        "conditions":{
            "door unlocked": True
        },
        "text": 
        """You open the door and see nothing. You can't control
        yourself and you go out. You see a field and the sky, but
        the sky is not blue. It looks like... .""",

        "GETs effect": {
            "outside open": True
        },
        
        "psychosis effect": 0,
        
        "remove after use": True,

        "items": []
    }
}

#Contains a list of all items in the game, with an identifier.
#Items must be put in this list to be usable.
#Item should be put in like this: "example": item_example
items = {
    "window": item_window,
    "wardrobe": item_wardrobe,
    "candle": item_candle,
    "clock": item_clock,
    "mirror": item_mirror,
    "writing": item_writing_on_wall,
    "medicine": item_medication,
    "coat": item_coat,
    "fusebox": item_fusebox,
    "vase": item_vase,
    "door": item_door,
    "picture": item_picture,
    "fuse": item_fuse,
    "markings": item_wall_markings,
    "magnifier": item_magnifying_glass,
    "book": item_book,
    "computer": item_computer,
    "paper": item_paper,
    "knife": item_knife,
    "bowl": item_bowl,
    "painting": item_painting,
    "key": item_key,
    "scarf": item_red_scarf,
    }