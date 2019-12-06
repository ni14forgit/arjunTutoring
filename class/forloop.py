# list of fruits
mylist = ["Apple","Banana","Orange","Strawberry"]

# the keyword elem is NOT tied to mylist!
# we can use any variable name

for elem in mylist:
    print(elem)

# output: "Apple" "Banana" "Orange" "Strawberry"


# len(mylist) takes in a list and outputs an integer, which is the length of the list
# range(size) takes in an integer and outputs a list up to that number
# ex: range(3) = [0,1,2]

for x in range(len(mylist)):
    print(x)

# output: 0, 1, 2, 3


# similar to the for loop above, but notice difference in print statement
# we are getting the element at each index rather than printing the index

for index in range(len(mylist)):
    print(mylist[index])

# output: "Apple" "Banana" "Orange" "Strawberry"


