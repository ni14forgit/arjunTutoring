def countDownFrom_N(number):
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



