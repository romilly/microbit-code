with open('log.txt') as f:
    print('data in log.txt:')
    while True:
        # try to read the next line
        line = f.readline()
        # see if there is any text
        if line:
            # if there is another line, print it 
            print(line.strip())
        else:
            # we're reached the end of the file, so stop looping
            break