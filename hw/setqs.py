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
