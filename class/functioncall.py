

# child and parent functions, fill out what they do. 

def child(): 
    return 5 

def parent(y):
    x = child()
    return x + y

# Simple recursive function, _______ fill out what it does
def printDownToZero(x):
    if x == -1: 
        return
    print(x)
    printDownToZero(x-1)


    



