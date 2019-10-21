#OS is used to interact with the command prompt window.
import os
#Keyboard is used to check keypresses.
import keyboard
#Time is used to prevent the keys from being detected constantly, makes menu usable.
import time
#Random is used for randomly changing colours.
import random
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

def update_display(logo, selection, options, footer, vertical_padding = 4):
    """This function updates the display for the main menu.
    It does this by clearing the screen and then reprinting the options in the correct configuration.
    """
    #Generate random colours for logo
    colours = random_colour_change()
    #Print spacing area
    print("\n" * int(vertical_padding))

    #Calculate the size of the logo
    logo_size = calc_logo_size(logo)
    #Calculate spacing required for logo
    logo_spacing = int((maxwidth - logo_size[0]) / 2)
    #Print the logo line by line
    for line in logo:
        print((" " * logo_spacing) + colours[0] + line + colours[1])
    
    #Print spacing area
    print("\n" * int(vertical_padding))
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
    #Print footer
    lines_taken_up = (vertical_padding * 2 + len(logo) + len(options) + 2)
    print("\n" * int(maxheight - lines_taken_up - 1))
    print(footer)

def key_press():
    if keyboard.is_pressed("w"):
        return "w"
    elif keyboard.is_pressed("s"):
        return "s"
    elif keyboard.is_pressed(" "):
        return " "
    else:
        return None

def random_colour_change():
    #Generates a random colour code for using with ansi escape codes to change colour
    return ["\x1b[" + str(random.randint(0,4)) + ";" + str(random.randint(30,38)) + ";" + str(40) + "m","\x1b[0m"]

def menu(options = ["New game ", "Load game", "Quit     "]):
    """Handles the main menu.
    When an option is selected and space or enter are pressed, 
    a number corresponding to the selected option is returned.
    Options can be configured by changing the options argument.
    """
    #Defines size of window
    os.system("mode con: cols="+ str(maxwidth) + " lines="+ str(maxheight))
    #String version of the game logo
    gamelogo = """
:::::::::   ::::::::  :::   :::  ::::::::  :::    :::  ::::::::   ::::::::  :::::::::::  :::::::: 
:+:    :+: :+:    :+: :+:   :+: :+:    :+: :+:    :+: :+:    :+: :+:    :+:     :+:     :+:    :+:
+:+    +:+ +:+         +:+ +:+  +:+        +:+    +:+ +:+    +:+ +:+            +:+     +:+       
+#++:++#+  +#++:++#++   +#++:   +#+        +#++:++#++ +#+    +:+ +#++:++#++     +#+     +#++:++#++
+#+               +#+    +#+    +#+        +#+    +#+ +#+    +#+        +#+     +#+            +#+
#+#        #+#    #+#    #+#    #+#    #+# #+#    #+# #+#    #+# #+#    #+#     #+#     #+#    #+#
###         ########     ###     ########  ###    ###  ########   ########  ###########  ######## """
    #Variable setup below
    #Split the logo into lines
    gamelogo = gamelogo.splitlines()
    current_selection = 0
    maximum_selection = len(options) - 1
    while True:
        #Main display loop
        os.system("cls")
        update_display(gamelogo, current_selection, options, "(C) No rights reserved. Using Pygame and Keyboard librarys.")
        keypressed = key_press()
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
        #Runs at 13.333 frames a second
        time.sleep(0.075)
    #This is a way of clearing the users input. Otherwise it would come up with all of the keys they pressed while in the menu after exiting it.
    keyboard.press_and_release('enter')
    input()
    os.system("cls")
    return options[current_selection]

def endscreen(mode):
    #Define size of window
    os.system("mode con: cols="+ str(maxwidth) + " lines="+ str(maxheight))
    #Win and lose ascci art as strings
    win_string = """
:::       ::: ::::::::::: ::::    :::
:+:       :+:     :+:     :+:+:   :+:
+:+       +:+     +:+     :+:+:+  +:+
+#+  +:+  +#+     +#+     +#+ +:+ +#+
+#+ +#+#+ +#+     +#+     +#+  +#+#+#
 #+#+# #+#+#      #+#     #+#   #+#+#
  ###   ###   ########### ###    ####"""
    lose_string = """
:::         ::::::::   ::::::::  ::::::::::
:+:        :+:    :+: :+:    :+: :+:       
+:+        +:+    +:+ +:+        +:+       
+#+        +#+    +:+ +#++:++#++ +#++:++#  
+#+        +#+    +#+        +#+ +#+       
#+#        #+#    #+# #+#    #+# #+#       
##########  ########   ########  ##########"""
    #Split both ascii art's into lines
    win = win_string.splitlines()
    lose = lose_string.splitlines()
    while True:
        os.system("cls")
        keypressed = key_press()
        if keypressed == " ":
            break
        if mode == "win":
            update_display(win, 0, [], "",(maxheight - calc_logo_size(win)[1]) / 2)
        elif mode == "lose":
            update_display(lose, 0, [], "",(maxheight - calc_logo_size(lose)[1]) / 2)
        time.sleep(0.075)