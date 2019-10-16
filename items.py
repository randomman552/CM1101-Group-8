item_medication = {
    #id of the room, is used as its name
    "id": "medication",
    #Name is shown when listing items from inventory
    "name": "your medication",
    #Description can be read with inspect command
    "description":
    """This is your medication""",
    #Weight is used with the inventory weight system, this can just be set to 0 if you dont want to use it
    "weight": 0
}

#Contains a list of all items in the game, with an identifier.
#Item must be put in this list to be usable.
#Item should be put in like this: "example": item_example
items = {
    "medication": item_medication
}