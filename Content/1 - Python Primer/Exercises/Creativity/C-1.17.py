# Had we implemented the scale function as follows, does it work properly?
def scale(data, factor):
    for val in data:
        val *= factor
# Explain why or why not.

# It will work properly if we use it properly. Of course if we use with mutable types
# we would just need to return the value and the new variable would be created
# but for immutable types we need to do it directly to the original variable.