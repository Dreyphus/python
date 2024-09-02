def getInput(l):
    try:
        l = int(l)
    except ValueError:
        #print('Please enter a valid number')
        newl = input('Please enter a valid number:')
        l = getInput(newl)
    
    return l