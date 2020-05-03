<<<<<<< HEAD
# Print out the number and call if
def answer(sequence, n):

    if n < 1:
        return sequence
    Else:

    #imagine for now sequence = [0,1]
    indexOfTheLastElement = len(sequence)-1
    lastElement = sequence[indexOfTheLastElement]
    secondToLastElement = sequence[len(sequence)-2]
    Newelem = lastElement + secondToLastElement
    sequence.add(newelem)
    answer(sequence, n-1)
=======
def ountDownFrom_N(number):
    # Line 3 is known as the "Base Case"
    if number < 1: 
        return 


    else: 
        print(number)
    # Line 10 is where we make the recursive call!
        countDownFrom_N(number-1)

countDownFrom_N(10)

'''
Fibonacci Numbers

What are they? -> Every number is the sum of the previous two numbers. 
*The first two elements of the sequence are 0, 1

Sequence -> 0 1 1 2 3 5 8 13 21 34 55 .... and so forth 

'''

# Make a recursive function that produces the first n elements of the fibonacci sequence. 


>>>>>>> b98449fd6454a6e0f70f78cee103899b4e3b690a

