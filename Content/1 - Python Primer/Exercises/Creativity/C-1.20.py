# Python's random module includes a function shuffle(data) that accepts a list
# of elements and randomly reorders the elements so that each possible order
# occurs with equal probability. The random module includes more basic function randint(a, b)
# that returns a uniformly random integer from a to b (including both endpoints).
# Using only the randint functio, implement your own version of the shuffle function.

import random


def randPositions(arr):
    newArr = []
    seen = set()
    for i in range(0, len(arr)):
        if arr[i] in seen:
            continue
        else:
            newArr.append(arr[random.randint(0, len(arr) - 1)])

    return newArr

arr = ['a', 'b', 'c', 'd']
newArr = randPositions(arr)
print(newArr)