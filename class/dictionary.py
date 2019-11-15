# This file will explain dictionaries!

# Store value in a dictionary and then retrieve them.

# In a dictionary or HashMap, a key maps to a value.
# You can set key-value pairs, and also retrieve values by the key.


# Line 10: Instantiate a empty dictionary called mydict
mydict = {}

# Line 13: Add a key-value pair "Arjun" -> "Pagidipati"
mydict["Arjun"] = "Pagidipati"

# Line 16: Print out the dictionary at this state
print(mydict)
# Output will be {"Arjun":"Pagidipati"}

# Line 19: Add key-value pair "Nishant" -> "Iyengar"
mydict["Nishant"] = "Iyengar"

# Line 23: Print out the dictionary at this state
print(mydict)
# Output will be {"Arjun":"Pagidipati", "Nishant":"Iyengar"}

# Line 27: Retrieve Arjun's last name
print(mydict["Arjun"])
# Will return "Pagidipati"

# Line 30: Rewrite key-value pair of "Arjun" to "Arjun"->"Duke"
mydict["Arjun"] = "Duke"

# Line 34: Print out the dictionary at this state
print(mydict)
# Output will be {"Arjun:Duke", "Nishant":"Iyengar"}

# Line 38: Add key-value pair "arjun" -> "Duke"
mydict["arjun"] = "Duke"

# Line 41: Print out the dictionary at this state
print(mydict)
# Output will be {"Arjun":"Duke", "Nishant":"Iyengar", "arjun":"Duke"}

# Line 45: Create a list of all the keys of the dictionary
print(mydict.keys())
#Output: ["Arjun", "Nishant", "arjun"]

# Line 49: Create a list of all the values of the dictionary
print(mydict.values())
#Output: ["Duke", "Duke", "Iyengar"]

# Line 53: Create key-value pair 9 -> "Arjun"
mydict[9] = "Arjun"
