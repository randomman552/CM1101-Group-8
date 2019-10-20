#OS is used to interact with the command prompt window.
import os
#Getch is used to get key presses (only works on windows, I will add code for other OS's shortly).
from msvcrt import getch
#Max width and height settings, used to define the size command prompt window and for positioning of UI elements.
maxwidth = 180
maxheight = 50
def calc_logo_size(logo_as_lines):
    """Gets the size of the logo inputted. Used in main menu
    The value is returned as a list with the width first, followed by the length
    """
    logo_width = len(logo_as_lines[1])
    logo_height = len(logo_as_lines)
    return [logo_width,logo_height]

def update_display(logo,selection,options):
    """This function updates the display for the main menu.
    It does this by clearing the screen and then reprinting the options in the correct configuration.
    """
    #Print spacing area
    print("\n\n\n\n")

    #Calculate the size of the logo
    logo_size = calc_logo_size(logo)
    #Calculate spacing required for logo
    logo_spacing = int((maxwidth - logo_size[0]) / 2)
    #Print the logo line by line
    for line in logo:
        print((" " * logo_spacing) + line)
    
    #Print spacing area
    print("\n\n\n\n")

    #Print menu
    for line in options:
        #Spacing is used to position the options centrally
        spacing = int((maxwidth - len(line)) / 2)
        #If the line is currently selected, add an indicator to show so
        #If it isnt, don't
        if line == options[selection]:
            print ((" " * (spacing - 1)) + ">" + line)
        else:
            print((" " * spacing) + line)

def key_press():
    #while True:
        #keys = pygame.key.get_pressed()
        #if keys[K_s]:
            #return "s"
        #elif keys[K_w]:
            #return "w"
        #elif keys[K_SPACE]:
            #return " "
    key = ord(getch())
    if key == 119:
        return "w"
    elif key == 115:
        return "s"
    if key == 32:
        return " "

def menu(options = ["New game ", "Load game", "Quit     "]):
    """Handles the main menu.
    When an option is selected and space or enter are pressed, 
    a number corresponding to the selected option is returned.
    Options can be configured by changing the
    """
    #Defines size of window
    os.system("mode con: cols="+ str(maxwidth) + " lines="+ str(maxheight))
    #String version of the game logo
    gamelogo = """
    :::::::::   ::::::::  :::   :::  ::::::::   ::::::::   ::::::::  :::::::::::  ::::::::   :::::::::  
    :+:    :+: :+:    :+: :+:   :+: :+:    :+: :+:    :+: :+:    :+:     :+:     :+:    :+: :+:     :+: 
    +:+    +:+ +:+         +:+ +:+  +:+        +:+    +:+ +:+            +:+     +:+               +:+  
    +#++:++#+  +#++:++#++   +#++:   +#+        +#+    +:+ +#++:++#++     +#+     +#++:++#++       +#+   
    +#+               +#+    +#+    +#+        +#+    +#+        +#+     +#+            +#+     +#+     
    #+#        #+#    #+#    #+#    #+#    #+# #+#    #+# #+#    #+#     #+#     #+#    #+#             
    ###         ########     ###     ########   ########   ########  ###########  ########      ###     

    """
    #Variable setup below
    #Split the logo into lines
    gamelogo = gamelogo.splitlines()
    current_selection = 0
    maximum_selection = len(options) - 1
    while True:
        #Main display loop
        os.system("cls")
        update_display(gamelogo,current_selection,options)
        keypressed = key_press()
        print(keypressed)
        if (keypressed == "s"):
            #If s pressed
            current_selection += 1
        elif (keypressed == "w"):
            #If w pressed
            current_selection -= 1
        elif (keypressed == " "):
            #If enter or space is pressed, the loop is broken.
            break
        #Check if current_selection is within its bounds.
        #If it isn't set it to the opposite extreme.
        if current_selection > maximum_selection:
            current_selection = 0
        elif current_selection < 0:
            current_selection = maximum_selection
    return options[current_selection]