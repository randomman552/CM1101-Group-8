import sys,time,random
typing_speed = 200 #wpm
def slow_print(text, type_print = False):
    """This function will type out the inputted string in the terminal if the second argument is true, otherwise it will print normally"""
    #If type_print is true, type the text out on the terminal.
    if not text == "":
        try:
            if type_print:
                for l in text:
                    sys.stdout.write(l)
                    sys.stdout.flush()
                    time.sleep(random.random()*5.0/typing_speed)
                print("")
            #If it is not, print the text normally.
            else:
                print(text)
        except TypeError:
            pass