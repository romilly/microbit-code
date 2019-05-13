from microbit import *

# log temperature evey second for one minute

# open a file for writing
with open('log.txt','w') as f:
    # loop for 60 readings
    for i in range(60):
        # read the temperature (Centigrade)
        temp = temperature()
        # format the text
        text = '%d C\n' % temp
        # log termperature
        f.write(text)
        # wait a second
        sleep(1000)