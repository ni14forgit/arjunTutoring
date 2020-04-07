# Given a list of name, and a set that contains some of those names
# Iterate over the elememnts of the list, and return a list of True/False that represents whether the set has that element


def removal():
    mylist = ["A", "B", "C", "D"]
    myset = set(["A", "C"])
    answer = []

    # mylist = [1,2,3,4,5]
    for a in range(len(mylist)):
        # CODE HERE:
        if mylist[a] in myset:
            answer.append(True)
        elif not mylist[a] in myset:
            answer.append(False)
    return(answer)

# return [True, False, True, False]




  

# Ouput all common names between the two lists 
# Order of the output does not matter
# Ex: 
# List A: ["Annie", "Sam", "Varun", "Calvin", "Neha", "Christina", "Chris"]
# List B: ["Arjun", "Annie", "Chris", "Nishant", "Rebecca"]
# Output: ["Annie", "Chris"]

def commonNames(A, B):
  	
    # myset = set()
    # myset.add("nishant")
    # if "nishant" in myset:
    #   print("myset contains nishant!")
    # if "rebecca" not in myset:
    #   print("myset does not contain rebecca, sad")
    
    # Pick a list and convert it to a set 
    # Iterate over the other list and check to see if the elements in the second list are in the set you just created
    # Instantiate an empty list 
    # If so, add those elements to a new (empty) list, and then return the new list
    
    listToReturn = []
    myset = set(A)
    for elem in B:
        if elem in myset:
            listToReturn.append(elem)

"""    
ARJUN's very own solution! 
Def commonnames(A, B):
            myset = set(A)
            listtoreturn = []
            For elem in B:
		        If elem in myset:
			        listtoreturn.append(elem)
"""
			

        
    #return(listToReturn)
      
    # Try to use a set 
    # Initialize an empty list 
    #pass






