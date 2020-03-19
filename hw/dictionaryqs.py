# Java mymap.put(key,value) -> Python mymap[key] = value
# Java mymap.get(key) -> Python mymap[key]
# Java if mymap.containsKey(key) -> Python if key in mymap


def answer():
    mymap = {}
    myarray = [1, 2, 3, 4, 5, 6, 6, 7, 8, 8]

    # for loop here, iterate over myarray
    # update mymap

    return mymap


# Sample problems

# Problem 1
# Create a method that return a dictionary that has all your family members names.

def Last_Names():
    mydict = {}
    names = ["Ishan", "Mom", "Dad"]
    for i in range(len(names)):
        mydict[names[i]] = "Pagidipati"
    return mydict


print(Last_Names())


'''November 15th, 2019'''

# Problem 2 // FINISHED

# Using a for loop (Hint: range(100)) create a dictionary that holds key-value pairs 1:1, 2:2, 3:3 and so on


def numbers():
    mydict = {}
    # Code to go here
    for a in range(100):
        mydict[str(a)] = a
    print(mydict)
    return mydict
numbers()

# Problem 3 // FINISHED

# Given any list of strings as an input, for ex: ["Arjun","Nishant","Amy","Bob"], return a dictionary with key value pairs name -> length of string.
# For example output would be {"Arjun:5,"Nishant":7,"Amy":3,"Bob":3}
# HINT: len(stringVariable) returns the length of the string

def names():
    mydict = {}
    namesList = ["Austin", "Cary", "Jerry", "Rahul", "Abby"]
    # Code goes here
    for i in range(len(namesList)):
        mydict[namesList[i]] = len(namesList[i])
    print(mydict)
    return mydict


# Problem 4: Given a list of names  with repeats, output the name with the most occurrences. 
#Ex: 
#Input: ["Sam", "Jon", "Tom", "Sam", "Sam", "Tom", "Sam", "Tom", "Jon", "Sam", "Sam", "Sam", "Jon", "Jon"]
#Output: "Sam" because it occurs the most often 

# x = ["Jon", "Jon", "Sam", "Tom"]
# x = {"Jon":2, "Sam":1, "Tom":3, "Rebecca":10}



def mostCommon(names):
    dict = {}
    length = len(names)
    for elem in names:
        if elem not in dict:
            dict[elem] = 1
        else:
            dict[elem] += 1
    greatest = 0
    nameToReturn = ""
    for elem in dict:
        if dict[elem] > greatest:
            greatest = dict[elem]
            nameToReturn = elem
    return(nameToReturn)
