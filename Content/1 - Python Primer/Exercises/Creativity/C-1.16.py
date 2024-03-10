# In our implementation of the scale function, the body of the loop executes the command data[j] *= factor. We have discussed that numeric types are immutable, and that the use of the *= operator in this context cause the creation of a new instance (not the mutation of an existing instance). How is it still possible, then, that our implementation of scale changes the actual parameter by the caller?

# If you are working with a immutable objects like tuples or strings, using *= wouldn't modify it.
# But you can modify it explicitly assigning the result to the original variable
# so the original modification could persist outside the function.

# Example

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

arr = [1, 2, 3, 4]
scale(arr, 2) # directly assigning the result to the variable
print(arr)  # output: [2, 4, 6, 8]
