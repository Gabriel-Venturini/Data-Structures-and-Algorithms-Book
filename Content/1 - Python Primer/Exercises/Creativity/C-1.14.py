# Write a short Python function that takes a sequence of integer values and determines if there is a distinct pair of numbers in the sequence whose product is odd.
import numpy as np


def isPairOdd(sequence):
    odd = []
    pair = []
    seen = set()
    for i in range(len(sequence)): # find the odd numbers
        if sequence[i] % 2 == 1:
            odd.append(sequence[i])

    for elemento in odd: # iterate the list
        if elemento not in seen: # add or remove the item if its on seen set
            seen.add(elemento)
            pair.append(elemento)
        else:
            seen.discard(elemento)
            while elemento in pair:
                pair.remove(elemento)
    
    return pair

sequence = [1,3,3,5,5,2,12,11,10]
result = isPairOdd(sequence)
print(result)