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


# Problem 2
#
