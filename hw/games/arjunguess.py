import random

guess = random.randint(1, 50)
print("choose a number between 1, 50: ")
userGuess = -1

while userGuess != guess:
    newguess = input()
    if newguess.isdigit():
        userGuess = int(newguess)
        if userGuess < 0 or userGuess > 50:
            print("Please enter a number in range")
            continue
    else:
        print("Please enter an actual number")
        continue

    if userGuess == guess:
        print("#U got it!Party!")
        exit()
    elif userGuess < guess:
        print("Too low")
    elif userGuess > guess:
        print("Too High")
