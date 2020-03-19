
# ''' a = [1, 2, 3, 4, 5,6,6,6,6,6,6,6]
# for r in range(len(a)):
#     print(a[r]) '''

# list1 = [1, 100, 3, 99, 5, 77]
# notEven = [1, 2, 3, 4, 5, 6, 7, 8]
# # give me the list [2,4,6] from notEven


# ''' for a in range(len(list1)):
#     if a != 5 or a != 3 or a != 1:
#         print(list1[a])
#  '''

# for a in range(len(notEven)):
#     if notEven[a] != 5 and notEven[a] != 3 and notEven[a] != 1:
#         print(notEven[a])


# ''' for a in range(len(list1)):
#     print(list1[a]) '''
# ''' 
# for number in range(5):
#     print(number) '''

# ''' for a in list1:
#     print(list1[a]) '''

# ''' r = True
# v = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 0
# while r:
#     print(v[n])
#     if n > 9:
#         r = False
#     n += 1
#  '''

# string1 = "abcd"
# string2 = "efgh"
# # produce the value "abgh"

# #ARJUN DID THIS YAY!!!
# #answer = string1[0:2] + string2[2:4] =
# answer = string1[:2] + string2[2:]

# x = "hello"

# # append to a list 


x = [1,2,3,4]
print("This is x before the for loop: " + str(x))
y = []
print("This is y before the for loop: " + str(y))
for elem in x: 
    y.append(elem+1)

print("This is x after the for loop: " + str(x))
print("This is y after the for loop: " + str(y))


# x = [1,2,3,4,5,6,7]
# x = x[0:len(x) - 1]

x = [1,2,3,4,5,6]
print("before: " + str(x))
x = x.pop(2)
print("after: " + str(x))

