# Demonstrate how to use Python's list comprehension syntax to produce this list:
# [0, 2, 6, 12, 20, 30, 42, 56, 72, 90]

# 2 - 0 = 2    --- 0 + 2 = 2
# 6 - 2 = 4    --- 2 + 4 = 6
# 12 - 6 = 6   --- 6 + 6 = 12
# 20 - 12 = 8  --- 12 + 8 = 20
# 30 - 20 = 10 --- 20 + 10 = 30
# 42 - 30 = 12 --- 30 + 12 = 42
# 56 - 42 = 14 --- 42 + 14 = 56
# 72 - 56 = 16 --- 56 + 16 = 72
# 90 - 72 = 18 --- 72 + 18 = 90

result = [i * (i + 1) for i in range(10)]
print(result)