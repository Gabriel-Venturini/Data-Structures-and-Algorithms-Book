# Write a Python function that takes a sequence of numbers and determines if all the numbers are different from each other (that is, they are distinct).

def isDistinct(sequence):
    seen = set()
    distinct = []
    for element in sequence: # iterate the list
        if element not in seen: # add or remove the item if its on seen set
            seen.add(element)
            distinct.append(element)
        else:
            seen.discard(element)
            while element in distinct:
                distinct.remove(element)

    if len(distinct) == len(sequence):
        return True
    return False

arr = [1,2,3,4,5,6,5]
new = isDistinct(arr)
print(new)



