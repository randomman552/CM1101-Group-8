import sys,time,random

typing_speed = 200 #wpm
def slow_print(text):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*5.0/typing_speed)
    print('')