# Make a list with Apples, Bannanas, 5 , 6 & 7
mylist = ["Apples", "Bannanas", "Lemons", 5, 6, 7]

for elem in range(len(mylist)):
    print(elem)
"""
       #   #
        # #
         #
"""
for elem in range(6):# Because the len(mylist) > 6
    print(elem)
# range(6) = [0, 1, 2, 3, 4, 5]
"""
       #   #
        # #
         #
"""
for elem in [0, 1, 2, 3, 4, 5]:
    print(elem)
"""
All of these return the same thing:

   #           #
    #         #
     #       #
      #     #
       #   #
        # #
         #

"""
"""
0
1
2
3
4
5
"""
#Translation:elem looks at the list, chooses the element at the index to the number of times the for loop is was run(elem is NOT a keyword).
#Page 1:
"""
##     ###   #   #  ###
# #   #   #  ##  #  #
#  #  #   #  # # #  ###
# #   #   #  #  ##  #
##     ###   #   #  ###
"""
for elem in ["Apples", "Bannanas", 5]:
    print(elem)
"""
       #   #
        # #
         #
"""
"""
Apples
Bannanas
5
"""
#Page 2:
"""
##     ###   #   #  ###
# #   #   #  ##  #  #
#  #  #   #  # # #  ###
# #   #   #  #  ##  #
##     ###   #   #  ###
"""
