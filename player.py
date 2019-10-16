from items import *
from map import rooms
from gameparser import *

#Settings for max carry weight and starting inventory
max_carry_weight = 2
inventory = []

# Start game at the reception
current_room = rooms["Start"]
