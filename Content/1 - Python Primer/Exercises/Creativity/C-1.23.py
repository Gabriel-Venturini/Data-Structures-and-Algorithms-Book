# Give an example of a Python code fragment that attempts to write an element
# to a list based on an index that may be out of bounds. If that index is out
# out of bounds, the program should catch the exception that results, and print
# the following message: "Don't try buffer overflow attacks in Python!"

arr = [1,2,3]
x = 3
i = 3
try:
    arr[i] = x
except IndexError as err:
    print("Don't try buffer overflow attacks in Python!")