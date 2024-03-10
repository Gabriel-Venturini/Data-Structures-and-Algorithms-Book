# The p-norm of a vector v = (v1, v2, ...) in n-dimensional space is defined as:
# || v || = p SQRT v1**p + v2**p + ... + vn**p.
# For the special case of p = 2, this results in the traditional Euclidean norm,
# which represents the length of the vector. For example, the Euclidean norm of
# a two-dimensional vector with coordinates (4, 3) has a Euclidean norm of
# SQRT 4**2 + 3**2 = SQRT 16 + 9 = SQRT 25 = 5.
# Give an implementation of a function named norm such that norm(v, p) returns
# the p-norm value of v and norm(v) returns the Euclidean norm of v.
# You may assume that v is a list of numbers.

import math

def norm(v, p=2): # 2 is the default Euclidean norm
    return math.sqrt(sum(x ** 2 for x in v)) # Euclidean norm

arr = [4, 3]
result = norm(arr)
print(result)