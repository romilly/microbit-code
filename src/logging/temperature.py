from microbit import *

def show(text):
    display.scroll(text)
    print('(%d,)' %text)

# loop forever
while True:
    # read the temperature (Centigrade)
    temp = temperature()
    # display temperature
    show(temp)
    # wait a second
    sleep(1000)