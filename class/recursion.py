# Print out the number and call if
Def answer(sequence, n):

    if n < 1:
        return sequence
    Else:

    #imagine for now sequence = [0,1]
    indexOfTheLastElement = len(sequence)-1
    lastElement = sequence[indexOfTheLastElement]
    secondToLastElement = sequence[len(sequence)-2]
    Newelem = lastElement + secondToLastElement
    sequence.add(newelem)
    answer(sequence, n-1)

