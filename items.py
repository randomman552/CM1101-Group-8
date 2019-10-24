def caesar_cipher(text, shift):
    text = text.lower()
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
            "meds used": True
        },
        
        "stage effect": 0,
        
        "sanity effect": 0,
        
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
        
        "sanity effect": 0,
        
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
    figure this out, might be a name...
    It reads: """ + caesar_cipher("sam", 1)
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
        
        "stage effect": 0,
        
        "sanity effect": 0,
        
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
        
        "stage effect": 0,
        
        "sanity effect": 0,
        
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

        "sanity effect": 0,

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
        "conditions":{
            "meds used": True
        },
        "text": "You put the coat on, you find its warmth comforting.",
        
        "GETs effect": {
            "coat on": True
        },
        
        "stage effect": 0,
        
        "sanity effect": 1,
        
        "remove after use": True,

        "items":[]
        }
    }

item_fusebox = {
    "id": "fusebox",
    
    "name": "a fusebox",
    
    "take": False,
    
    "description":
    """A red fusebox on the wall... Looking at the inside you see that one of the fuses is missing
You make a mental note to find it...""",
        
    "inspection":
    """You notice the fusebox looks very old, it's even rusting in places...
That cant be good..."""
    }

item_fuse = {
    "id": "fuse",

    "name": "a fuse",

    "take": True,

    "weight": 0,

    "description":
    """A fuse... Perhaps there is somewhere to put it...""",

    "inspection":
    """The fuse is rectangular in shape, exposed contacts can be seen at either end.""",

    "use": {
        "conditions": {
            "items":[item_fusebox]
        },
        
        "text":
            """You pry open the fusebox with your finger nails and push the fuse you found in the living room into the one empty slot.
The lights suddenly flicker back on, you won't need this candle anymore.""",

        "GETs effect": {
            "computer on": True
        },
        
        "stage effect": 0,
        
        "sanity effect": 0,
        
        "remove after use": True,

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
        
        "sanity effect": 0,

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
        "It's just a small key"
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

    "name": "a magnifying glass",
    "take": True,

    "weight": 0,

    "description":
    """I might be able to use this help with inspecting things...""",
    "inspection": "You can't use a magnifying glass to look at itself!!!"
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

    "inspection":
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

        "text": """Hello! How do you find our puzzles? You might be tired,
the transfer process wasn't an easy one. Recover yourself and get out of here.
The more time you spend in this house, harder will be to come back to life.
If we can solve the puzzles and go out, we deserve it! Don't forget about the
pills. They are behind the mirror. There is a chance some programmes have some
failures, but the environment won't affect you. I just hope you remember... .
Otherwise, you have to complete every quest or the computer will erase us.
One last thing! You have placed some clues in the puzzles in order to help
you remember. Use them wise, they don't last for long!""",

        "GETs effect": {
            "computer used": True
        },

        "remove after use": True,

        "sanity effect": 1,

        "items":[]
        },
    #The answer to the riddle on the paper is "dream"
    #The answer to the number sequence puzzle in the book is 445
    "password" : "dream445" 
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
        
        "sanity effect": -6,
        
        "remove after use": False,
        }
    }

item_empty_bowl = {
    "id": "bowl",

    "name": "an empty bowl",

    "take": True,

    "description": "That was some top notch food.",

    "inspection": "You can see scratches etched into the bottom of the bowl from years of use."
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
        """It also tastes like my mum's. Weird.""",

        "GETs effect": {},
        
        "sanity effect": 1,
        
        "remove after use": True,

        "items":[item_empty_bowl]
        }
    }

item_painting = {
    "id": "painting",

    "name": "a painting",

    "take": False,

    "description":
    """The painting reads "Retro Bazinga!".
It looks like someone was a fan of computer games.""",

    "inspection":
    """The name 'Kirill' is etched onto the frame in very small writing."""
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
            "meds used": True
        },
        "text": 
        """You open the door to the outside world, after you put on your coat, it's time to leave.""",

        "GETs effect": {
            "outside open": True
        },
        
        "sanity effect": 0,
        
        "remove after use": True,

        "items": []
    }
}

#Contains a list of all items in the game, with an identifier.
#Items must be put in this list to be usable.
#Item should be put in like this: "example": item_example
items = {
    "medication":item_medication,
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