# # Problem 1,2,3
# # Without running the programs, comment what the programs forLoop(), forLoop2(), and forLoop3() outputs


# def forLoop():
#     mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
#     for elem in mylist:
#         print(elem)
# forLoop()

# # Answer for forLoop():
# #The output will be "Apples", "Banana", "Lemons", 5, 6, 7.


# def forLoop2():
#     mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
#     for elem in range(len(mylist)):
#         print(elem)
# forLoop2()

# # Answer for forLoop2():
# #The output will be "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7.

# def forLoop3():
#     mylist = ["Apples", "Banana", "Lemons", 5, 6, 7]
#     for elem in range(len(mylist)-2):
#         print(elem)
# forLoop3()

# # Answer for forLoop3():
# #The output will be "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7, "Apples", "Banana", "Lemons", 5, 6, 7.

# for elem in ["Apples", "Bananas", 5]:
#     print(elem)

# print(["Apples", "Bananas", 5])

# for elem in [0,1,2,3,4,5]:
#     print(elem)
#     print('hi')

# mylist = [33,44,55,66,77]
# print(mylist[-6])


# February 13th, 2020

# Homework Problem 1
# Given a list of names, print all the names that have an odd number of characters.
# #Ex: mylist = ["nishant", "arjun", "sara", "mark", Rachel, Ola] => prints first two and last two names
# def oddnames(mylist):
#     for elem in len(range(mylist)):
#         #if len(mylist[elem]) == 1 or len(mylist[elem]) == 3 or len(mylist[elem]) == 5 or len(mylist[elem]) == 7:
#         if len(mylist[elem])%2 == 1:
#             print(elem)

   

# # Homework Problem 2
# # Given a list, slice it and return the second half of the list (includes middle element if length of list is odd).
# #Ex: mylist = [1,2,3,4,5,6,7] => returns [4,5,6,7]
# def slicelist(mylist):
#     len1 = len(mylist)
#     len2 = len1/2
#     secondhalf = mylist[len2:len1]
#     print(secondhalf)
#     pass 


# Given an input list and mod m, return a list of elem % m for every elem in the input.
def modandappend(input_list, m):
    print("this is input list: " + str(input_list))
    print("this is the mod value " + str(m))
    newlist = []
    #Code goes here
    for elem in input_list:
        newelem = elem % m
        newlist.append(newelem)
    print("this is newlist: " + str(newlist))
    return newlist

modandappend([1,2,3,4,5,6,7,8,9,10], 3)