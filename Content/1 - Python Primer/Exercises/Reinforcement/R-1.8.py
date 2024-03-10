# Python allows negative integers to be used as indices into a sequence, such as a string. if string s has length n, and expression s[k] is used for index -n <= k < 0, what is the equivalent index j >= 0 such that s[j] references the same element?


arr = [1, 2, 3, 4] # -4, -3, -2, -1 / 0, 1, 2, 3
print(len(arr))

# Answer: we can use the formula j = n + k
# For example, the length of arr is 4 and I want to find the corresponding positive index
# to s[-2], so I would do j = 4 + (-2) and it would give me s[2] that corresponds with
# the element s[-2] = 3 and element s[2] = 3