# This file will introduct sets in Python!

myset = set()

myset.add("Arjun")

print(myset)

myset.add("Arjun")

print(myset)

myset.add("arjun")

print(myset)

myset.remove("arjun")

print(myset)

# myset.remove("Nishant")
# CRASH!!! "Nishant was not in the file!"

# Check to see if in an element is inside the set
# Returns a boolean, TRUE if the element is inside the set.

print("Arjun" in myset)
