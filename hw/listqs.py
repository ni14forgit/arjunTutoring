# Problem 1,2,3
# Without running the programs, comment what the programs forLoop(), forLoop2(), and forLoop3() outputs


def forLoop():
    mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
    for elem in mylist:
        print(elem)

# Answer for forLoop():


def forLoop2():
    mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
    for elem in range(len(mylist)):
        print(elem)

# Answer for forLoop2():


def forLoop3():
    mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
    for elem in range(len(mylist)-2):
        print(elem)

# Answer for forLoop3():
