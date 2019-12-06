# Problem 1,2,3
# Without running the programs, comment what the programs forLoop(), forLoop2(), and forLoop3() outputs


def forLoop():
    mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
    for elem in mylist:
        print(elem)
forLoop()

# Answer for forLoop():
#The output will be "Apples", "Banana", "Lemons", 5, 6, 7.


def forLoop2():
    mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
    for elem in range(len(mylist)):
        print(elem)
forLoop2()

# Answer for forLoop2():
#The output will be "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7.

def forLoop3():
    mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
    for elem in range(len(mylist)-2):
        print(elem)
forLoop3()

# Answer for forLoop3():
#The output will be "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7.
