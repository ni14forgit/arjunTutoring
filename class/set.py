# This file will introduct sets in Python!

# make a new set
myset = set()

# Add an element called "Arjun"
myset.add("Arjun")

print(myset)

# Add an element called "Arjun", there will still only be one Arjun, because this is a set.
myset.add("Arjun")

print(myset)

# Adding the element "arjun" which is DIFFERENT from "Arjun"
myset.add("arjun")

print(myset)

# Removes "arjun"
myset.remove("arjun")

print(myset)

# myset.remove("Nishant")
# #CHRASH "Nishant" WAS NOT IN THIS SET


"Arjun" in myset
# Returns True if "Arjun" is in myset, or False if not.

if "Arjun" in myset:
    myset.remove("Arjun")
