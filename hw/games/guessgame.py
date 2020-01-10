# Create a game that creates a number and then asks the user to guess that number until they get it
# The program should reply whether the guess is too low or too high

# Starter Code

import random

# make a random
guess = random.randint(0, 100)
# tell the player to guess a random number
print("I made a number 0,100 : can you guess it?")
# set the user's guess to something that will never be guess
userGuess = -1

# make a while loop
while userGuess != guess:

    # OPTIONAL: think about how to handle user input that is not a number?
    # Look online and try things that you find!

    # make newguess
    newguess = input()
    #
    if newguess.isdigit():
        userGuess = int(newguess)
        if userGuess < 0 or userGuess > 100:
            print("Your number is not in the range, please provide a number in range.")
            continue
    else:
        print("Please provide an actual number")
        continue

    # Complete the rest of the logic, to write whether too low or too high

    if userGuess == guess:
        print("Yay!U got it")
        exit()
    elif userGuess < guess:
        print("Too low")
    else:
        print("Too high")

    #
