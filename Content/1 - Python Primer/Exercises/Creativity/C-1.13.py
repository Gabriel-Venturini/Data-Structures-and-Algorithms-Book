# Write a pseudo-code description of a function that reverses a list of n integers, so that the numbers are listed in the opposite order than they were before, and compare this method to an equivalent Python function for doing the same thing.
import numpy as np

def reverse(arr):
    # Receives the list of integers and uses a while loop
    # starting from the last index to the first one
    # then appends the number to the new list
    # returns the new list
    newArr = []
    i = -1
    while i >= -len(arr):
        newArr.append(arr[i])
        i -= 1
    return newArr


arr = [1,2,3,4]
result = reverse(arr)
print(result)

# Otherwise we can use a lib called numpy to flip a array and a method called flip()
# with this method the numbers are not organized with commas between then
# and you need to import it into your code

newlist = [4,3,2,1]
fliplist = np.flip(newlist)
print(fliplist)