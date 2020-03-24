

# child and parent functions, fill out what they do. 

def child(): 
    return 5 

def parent(y):
    x = child()
    return x + y

parent(8)

#_______________________________________________#


#Python picks variables first instantiated in the function, and then global variables (variables instantiated outside of the function). 


# Example to teach simple scoping, Arjun got them right 

# x = "nishant"
# def function_one(y): 
# 	global x
# print(x)

# function_one(“Arjun”)




#_______________________________________________#


#Make the happy birthday song with 
#Happy Birthday to you, Happy Birthday to you, Happy birthday dear Arjun, happy birthday to you. Eat More Chicken!

def birthday_one():
    print("Happy Birthday to you")

def birthday_two(name):
	print("Happy birthday dear " + name)

def birthday_three():
	print("Eat More Chicken!")

name = input()

# def birthday():
#     global name
#     birthday_one()
#     birthday_one()
#     birthday_two(name)
#     birthday_one()
#     birthday_three()
#     birthday()


#___________________________________________________________#

# Simple recursive function, _______ fill out what it does
def printDownToZero(x):
    if x == -1: 
        return
    print(x)
    printDownToZero(x-1)


    



